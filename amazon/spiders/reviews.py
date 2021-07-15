import scrapy
from scrapy.utils.response import open_in_browser

reviews_url = 'https://www.amazon.com/product-reviews/{}'

# Can change ASIN number based on product
asin_list = ['B08G9J44ZN']


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests(self):
        for asin in asin_list:
            url = reviews_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        for review in response.css('[data-hook="review"]'):
            open_in_browser(response)
            item = {
                'name': review.css('.a-profile-name ::text').get(),
                'stars': review.css('[data-hook="review-star-rating"] ::text').get(),
                'title': review.css('[data-hook="review-title"] span ::text').get(),
                'review': review.xpath('normalize-space(.//*[@data-hook="review-body"])').get(),
            }
            yield item

        next_page = response.xpath('//a[text()="Next page"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
