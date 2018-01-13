## huxiu

爬取huxiu——电商消费模块数据

在https://www.huxiu.com/channel/103.html页面，每次ajax请求有14个数据
一共有60页
所以一共有 14*60 = 840个数据

-> 寻找ajax请求地址以及传入的参数组
-> 在chrome console Elements页面上找到了https://www.huxiu.com/channel/ajaxGetMore 地址，并测试可以通过该div块的click的操作进行数据加载
var sub = document.getElementById("get_data”);
sub.click()
->  在network模块中Name列找到了ajaxGetMore的链接 并在Headers模块中找到了Form data的数据
-> 使用postman模拟客户端进行post请求，并填入已知参数
-> 获得返回数据
-> 使用scrapy shell来验证相应的xpath规则表达式
-> 在scapy工程中进行持久化操作
-> 完成
