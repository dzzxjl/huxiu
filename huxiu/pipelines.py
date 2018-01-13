# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HuxiuPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host='39.108.106.20', user='root', password='123456', db='huxiu', charset='utf8')
        cursor = db.cursor()
        # sql = 'INSERT INTO comment(content) VALUES (%s)'
        sql = 'INSERT INTO huxiu(title,time,author,collection_num,comment_num,content,url,category) ' \
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        # sql = 'INSERT INTO comment(content,time) VALUES (%s,%s)'
        # try:
        title = item['title']
        time = item['time']
        author = item['author']  # 作者
        collection_num = item['collection_num']  # 收藏数
        comment_num = item['comment_num']  # 评论数
        content = item['content']  # 内容
        url = item['url']  # 原文url
        category = item['category']  # 种类
        cursor.execute(sql, (title, time, author, collection_num, comment_num, content, url, category))
        db.commit()
        # except:
            # 发生意外，则回滚
        print('插入数据库时，发生错误')
        db.rollback()
        db.close()

        return item
