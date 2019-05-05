from scrapy.spiders import Spider
from ..items import SpiderPmItem

# 获取pm2.5的数据
class SpiderPm(Spider):
    name = 'spiderpm'  # 爬虫名字
    allowed_domains = ['www.pm25.com']  # 指定的域名
    start_urls = ['http://www.pm25.com/rank.html']  # 请求的url

    def parse(self, response):
        result = response.xpath('//ul[@class="pj_area_data_details rrank_box"]/li')
        for item in result:
            spiderpm = SpiderPmItem()
            spiderpm['date'] = response.xpath('//div[@class="rank_banner_right"]/span/text()').extract_first()  # 时间
            spiderpm['ranking'] = item.xpath('./span[@class="pjadt_ranknum"]/text()').extract_first()  # 排名
            spiderpm['state'] = item.xpath('./span[@class="pjadt_quality"]/em/text()').extract_first()  # 状况
            spiderpm['city'] = item.xpath('./a[@class="pjadt_location"]/text()').extract_first()  # 城市
            spiderpm['province'] = item.xpath('./span[@class="pjadt_sheng"]/text()').extract_first()  # 省份
            spiderpm['AQI'] = item.xpath('./span[@class="pjadt_aqi"]/text()').extract_first()  # aqi
            spiderpm['chroma'] = item.xpath('./span[@class="pjadt_pm25"]/text()').extract_first()  #浓度
            print(spiderpm)
            yield spiderpm
            pass
        pass
    pass
