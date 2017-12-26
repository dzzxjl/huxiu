#coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider

from huxiu.items import HuxiuItem

class Huxiu(CrawlSpider):
    name = 'huxiu'
    url_list = []
    with open("./huxiu_103_list_1.txt", 'r') as file:
        for line in file:
            # print(line)
            line = line.strip("\n")
            url_list.append(line)
    # start_urls = ['https://www.huxiu.com/article/227116.html']
    start_urls = ['https://www.huxiu.com/article/' + x + '.html' for x in url_list]

    # def parse(self, response):
    #     yield scrapy.Request("https://www.huxiu.com/article/227184.html", callback=self.parse_content)


    def parse(self, response):

        item = HuxiuItem()
        selector = scrapy.Selector(response)
        # print(response)
        title = str(selector.xpath('//h1[@class="t-h1"]/text()').extract()[0]).strip('\n').strip()
        time = selector.xpath('//span[@class="article-time pull-left"]/text() | //span[@class="article-time"]/text()').extract()[0]
        author = selector.xpath('//span[@class="author-name"]/a/text()').extract()[0]
        collection_num = selector.xpath('//span[@class="article-share pull-left"]/text() | //span[@class="article-share"]/text()').extract()[0].strip("收藏")
        comment_num = selector.xpath('//span[@class="article-pl pull-left"]/text() | //span[@class="article-pl"]/text()').extract()[0].strip("评论")
        content = selector.xpath('//div[@class="article-content-wrap"]/p/text()').extract()

        content_all = ''
        for x in content:
            content_all = content_all + x
        url = 'url' # 原文url
        content = content_all

        category = selector.xpath('//div[@class="column-link-box"]/a/text()').extract()
        category_all = ''
        for x in category:
            category_all = category_all + x
        category = category_all

        print(title)
        # 填入item
        item['title'] = title
        item['time'] = time
        item['author'] = author
        item['collection_num'] = collection_num
        item['comment_num'] = comment_num
        item['content'] = content
        item['url'] = url
        item['category'] = category

        yield item
        url_next = "https://www.huxiu.com" + selector.xpath('//div[@class="hot-article-img"]/a/@href').extract()[0]
        print("@@@@@@@@@@@@@@@2", url_next)
        yield scrapy.Request(url_next, callback=self.parse)


        # class Jianshu(CrawlSpider):
#     # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字
#     name='huxiu'
#     # 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取
#     start_urls=['https://www.huxiu.com/article/209794.html']
#
#     url = 'http://www.huxiu.com'
#
#     # 每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数
#     # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象
#     def parse(self, response):
#         # item对象是自定义的python字典
#         item = HuxiuItem()
#         selector = scrapy.Selector(response)
#         article = selector.xpath('//div[@class="article-wrap"]')
#         # for article in articles:
#
#         # title = article.xpath('h1/text()').extract()
#         title = selector.xpath('/html/head/title/text()').extract()
#         author = article.xpath('div[@class="article-author"]/span/a/text()').extract()
#         # content = article.xpath('div[@class="article-content-wrap"]/text()').extract()
#         content = selector.xpath('//p/text()').extract()
#         url = 'url'
#         category = 1
#         item['title'] = title
#         item['author'] = author
#         item['content'] = content
#         item['url'] = url
#         item['category'] = category
#         # print(item)
#         yield item


        #....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据