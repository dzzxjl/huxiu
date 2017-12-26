from scrapy import cmdline


name = 'huxiu'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())