# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MytuneiItem(scrapy.Item):
    # define the fields for your item here like:
    myurl = scrapy.Field()
    mytext = scrapy.Field()
    myimg = scrapy.Field()
    image_path = scrapy.Field()


# class MytuneiItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
