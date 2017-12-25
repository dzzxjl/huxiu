# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class HuxiuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field() # 标题
    time = Field() # 时间
    author = Field() # 作者
    collection_num = Field() # 收藏数
    comment_num = Field() # 评论数
    content = Field() # 内容
    url = Field() # 原文url
    category = Field() # 种类
