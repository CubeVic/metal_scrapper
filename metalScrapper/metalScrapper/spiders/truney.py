# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from metalScrapper.items import Truney


class TruneySpider(scrapy.Spider):
    name = "truney"
    allowed_domains = ["www.truney.com"]
    start_urls = ["https://www.truney.com/en/shop/category/silver-2",
                  "https://www.truney.com/en/shop/category/gold-1",
                  "https://www.truney.com/en/shop/category/other-precious-metals-platinum-39",
                  "https://www.truney.com/en/shop/category/other-precious-metals-palladium-40",
                  "https://www.truney.com/en/shop/category/other-precious-metals-copper-42",
                  "https://www.truney.com/en/shop/category/collectible-coins-30"]

    def parse(self, response):
        for item in response.xpath("//tbody/tr"):
            il = ItemLoader(item=Truney(), selector=item)
            il.add_css('name', 'h6')
            il.add_css('price', 'span[data-oe-type="monetary"]>span')
            il.add_css('url', 'a[itemprop="url"]::attr(href)')
            yield il.load_item()

        next_page = response.xpath(
            '//ul[contains(@class,"pagination")]/li[last()]/a').attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
