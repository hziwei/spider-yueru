from scrapy import cmdline
import time
cmdline.execute('scrapy crawl spiderfan'.split())  # 爬取租房信息
# cmdline.execute('scrapy crawl spiderpm'.split())  # 爬取pm2.5
