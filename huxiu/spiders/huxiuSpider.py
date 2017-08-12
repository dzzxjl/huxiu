#coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from huxiu.items import HuxiuItem
import urllib

class Jianshu(CrawlSpider):
    name='huxiu'   # 运行时这个爬虫的名字
    start_urls=['https://www.huxiu.com/article/209794.html']
    url = 'http://www.huxiu.com'

    def parse(self, response):
        item = HuxiuItem()
        selector = scrapy.Selector(response)
        article = selector.xpath('//div[@class="article-wrap"]')
        # for article in articles:
        title = article.xpath('h1/text()').extract()

        author = article.xpath('div[@class="article-author"]/span/a/text()').extract()
        content = article.xpath('div[@class="article-content-wrap"]/text()').extract()
        url = 'url'
        category = 1
        item['title'] = title
        item['author'] = author
        item['content'] = content
        item['url'] = url
        item['category'] = category
        print(item)
        yield item





        #....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据

