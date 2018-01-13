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

