import jieba

with open('../article.txt', 'r', encoding='utf8') as file:

    map = {}
    for line in file:
        par = line.split("。")
        for s in par:
            seg_list = jieba.lcut(s, cut_all=False)

            print(s)
            # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
            for x in seg_list:
                print(x)
                if x not in map:
                    map[x] = 1
                else:
                    map[x] = map[x] + 1


print(map)
ming_map_sorted = sorted(map.items(), key=lambda item:item[1], reverse=True)
print(ming_map_sorted)