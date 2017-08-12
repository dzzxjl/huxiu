# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class HuxiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field() # 标题
    author = Field() # 作者
    content = Field() # 内容
    url = Field() # url链接
    category = Field() # 种类
