from w3lib.html import remove_tags

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class PredioItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()

    url = scrapy.Field()


class PredioItemLoader(ItemLoader):
    default_item_class = PredioItem
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(remove_tags, str.strip)

    description_out = Join('\n')