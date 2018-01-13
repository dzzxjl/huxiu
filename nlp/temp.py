# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 20:58
# @Author  : dzzxjl@126.com


import jieba
import jieba.analyse
from os import listdir
import sys

files = [f for f in listdir(sys.path[0])]
print(files)

with open('./article.txt', 'r', encoding='utf8') as file:
    map = {}
    for line in file:
        result = jieba.analyse.extract_tags(line, topK=20, withWeight=False, allowPOS=())
        # print('haha')
        for x in result:
            print(x)

            # par = line.split("。")
            # for s in par:
            #     seg_list = jieba.lcut(s, cut_all=False)
            #
            #     print(s)
            #     # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
            #     for x in seg_list:
            #         print(x)
            #         if x not in map:
            #             map[x] = 1
            #         else:
            #             map[x] = map[x] + 1

            #
            # print(map)
            # ming_map_sorted = sorted(map.items(), key=lambda item:item[1], reverse=True)
            # print(ming_map_sorted)