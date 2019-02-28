from scrapy import Spider
from adondevivir.items import PredioItemLoader

class AdondeVivirSpider(Spider):
    name = 'adondevivir'
    start_urls = []
    