import scraper_helper as sh

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'
ROBOTSTXT_OBEY = False
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 2
DEFAULT_REQUEST_HEADERS = sh.get_dict(

    '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
sp-cdn="L5Z9:CA"; ubid-main=130-1295885-2116668; csm-hit=tb:950J5ES2BKVQS1HBDF44+s-950J5ES2BKVQS1HBDF44|1625013306681&t:1625013306681&adb:adblk_no
downlink: 10
ect: 4g
rtt: 100
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
'''
)
