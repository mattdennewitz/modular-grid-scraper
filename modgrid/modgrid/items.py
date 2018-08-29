# -*- coding: utf-8 -*-
import scrapy


class ModGridItem(scrapy.Item):
    manufacturer = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
