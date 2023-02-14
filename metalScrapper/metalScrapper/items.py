# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from itemloaders.processors import MapCompose
from itemloaders.processors import TakeFirst
from w3lib.html import remove_tags

def cast_to_float(price :str) -> float:
	price = price.replace(",","")
	return float(price)


class Truney(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, cast_to_float), output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

class Kitco(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
