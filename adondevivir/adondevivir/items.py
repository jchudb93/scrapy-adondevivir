
import scrapy
from scrapy.loader import ItemLoader


class PredioItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()

    url = scrapy.Field()


class PredioItemLoader(ItemLoader):
    default_item_class = PredioItem
