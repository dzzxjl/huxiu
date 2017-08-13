#coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider

from huxiu.items import HuxiuItem


class Jianshu(CrawlSpider):
    # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字
    name='huxiu'
    # 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取
    start_urls=['https://www.huxiu.com/article/209794.html']

    url = 'http://www.huxiu.com'

    # 每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数
    # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象
    def parse(self, response):
        # item对象是自定义的python字典
        item = HuxiuItem()
        selector = scrapy.Selector(response)
        article = selector.xpath('//div[@class="article-wrap"]')
        # for article in articles:

        # title = article.xpath('h1/text()').extract()
        title = selector.xpath('/html/head/title/text()').extract()
        author = article.xpath('div[@class="article-author"]/span/a/text()').extract()
        # content = article.xpath('div[@class="article-content-wrap"]/text()').extract()
        content = selector.xpath('//p/text()').extract()
        url = 'url'
        category = 1
        item['title'] = title
        item['author'] = author
        item['content'] = content
        item['url'] = url
        item['category'] = category
        # print(item)
        yield item





        #....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据

