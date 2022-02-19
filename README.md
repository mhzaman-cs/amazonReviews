# Amazon Reviews Scraper

The Amazon Reviews Scraper scrapes customer reviews about specific products from Amazon's online store using scrapy. This is a commonly posted freelance task. It allows users to download as many Amazon reviews as they would like based on the product's ASIN (Amazon Standard Identification Number), which is a 10-digit alphanumeric product identifier code issued by Amazon to every unique item offered in its catalog and housed in its warehouses. The scraped data can be stored in different formats, eg. CSV, XML, SQL, XLS, etc. The program also opens Amazon's website on the browser to avoid getting caught in Amazon's Captcha trap and continue downloading reviews.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- The first requirement is to have any version of python3 downloaded on the device the program will be run on.
- The second requirement would be to download Scrapy.
- The last requirement is scraper-helper

### Installing
Python can be done off the following link: [https://www.python.org/downloads/](https://www.python.org/downloads/).


Scrapy can be downloaded using the following commands in the command prompt:

With pip:
```
> pip install scrapy
```
With conda:
```
> conda install -c conda-forge scrapy
```


scraper-helper can be downloaded using the following commands in the command prompt:

With pip:
```
> pip install scraper-helper
```

## Deployment
1. To deploy the scraper cd into the correct file directory in the command prompt
2. Open the folder in a code editor of your choice, eg. Atom, Visual Studio Code, etc.
3. Go to reviews.py in the following manner, amazonReviews-master -> amazon -> spiders -> reviews.py
4. Change the values in the asin_list to the values you would like to scrape. If you would like to scrape reviews for more that 1 value add it to the list. Besure to remove the placeholder value of 'B08G9J44ZN'
5. Then run the following command in the command line, replacing FILE_NAME with the name of the file that you would like to save it as, and replacing tfile with the type of the file, eg. csv, sql, xml, the file will be saved in the project folder:
```
> scrapy crawl reviews -o FILE_NAME.tfile
```

## Demo
[<img src="Demo.gif" width="100%"/>](https://github.com/MuhammadZ985/amazonReviews)

## Built With

* [python3](https://www.python.org/downloads/) - The language used
* [scrapy](https://scrapy.org/) - First Dependency
* [scraper-helper](https://pypi.org/project/scraper-helper/) - Secondary Dependency

## Authors

* **Muhammad Zaman** - *Sole Creator* - [Muhammad Zaman](https://github.com/MuhammadZ985)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
