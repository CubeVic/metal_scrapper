# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from metalScrapper.items import Kitco


class KitcoSpider(scrapy.Spider):
    name = "kitco"
    allowed_domains = ["kitcoasiametals.com"]
    start_urls = ["https://kitcoasiametals.com/tw/ProductCategory/silver",
                  "https://kitcoasiametals.com/tw/ProductCategory/gold",
                  "https://kitcoasiametals.com/tw/ProductCategory/platinum",
                  "https://kitcoasiametals.com/tw/ProductCategory/palladium",
                  "https://kitcoasiametals.com/tw/ProductCategory/rhodium"]

    def parse(self, response):
        for item in response.css(
                'div.row>div[class*="col"]>div[class*="productItem"]'):
            il = ItemLoader(item=Kitco(), selector=item)
            il.add_css(field_name="name", css="div.text-area>p.title-1")
            il.add_css(field_name="price", css="div.text-area>p.price")
            il.add_css(field_name="url",
                       css="div.productImageBox>a::attr(href)")
            yield il.load_item()
