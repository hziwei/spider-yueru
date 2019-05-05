import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
import re
from ..items import SpideryueruItem


class SpiderFan(CrawlSpider):
    name = 'spiderfan'  # 爬虫名字
    allowed_domains = ['www.yueru.com']  # 域名
    start_urls = ['http://www.yueru.com/Room']

    rules = (
        Rule(
                LinkExtractor(allow='/index.html', unique=True),
                follow=True,  # 指定回调函数
                callback='parse_info',  # 指定回调函数
                process_links='get_url',  # 对提取的url做额外的处理
                # process_request='',  #对页面进行额外的操作
        ),
    )

    @staticmethod
    def get_url(links):
        url_list = []
        for link in links:
            if re.findall('\?_rgid=\d+&page=\d+',link.url):
                url_list.append(link)
                pass
            pass
        return url_list
        pass

    @staticmethod
    def parse_info(response):
        result = response.xpath('//div[@class="w1200"]/ul[@class="home2_list cf"]/li')
        for item in result:
            spider = SpideryueruItem()
            spider['zone'] = response.xpath('//a[@class="cur"]/text()').extract()[1]
            spider['title'] = item.xpath('.//div[@class="f_r"]/h4/a/span/text()').extract_first().strip()  # 标题
            spider['village'] = item.xpath('.//div[@class="f_r"]/p[1]/a/em/text()').extract_first().strip()  # 地区
            spider['area'] = item.xpath('.//div[@class="f_r"]/p[2]/text()').extract_first().strip()  # 面积
            spider['type'] = item.xpath('.//div[@class="f_r"]/p[2]/span/text()').extract()  # 类型
            spider['fenge'] = item.xpath('.//div[@class="f_r"]/p[3]/text()').extract_first().strip()  # 风格
            spider['ruzhu'] = item.xpath('.//div[@class="f_r"]/p[3]/span/text()').extract_first().strip()  # 入住时间
            spider['tese'] = item.xpath('.//div[@class="f_r"]/p[4]/i/text()').extract_first()  # 特色
            spider['addr'] = item.xpath('.//div[@class="f_r"]/p[5]/text()').extract_first().strip()  # 地址
            spider['price'] = item.xpath('.//div[@class="f_r"]/div/em/text()').extract_first().strip()  # 价格
            yield spider
            pass
        pass
    pass
