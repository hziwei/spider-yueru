# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpideryueruItem(scrapy.Item):
    _id = scrapy.Field()
    zone = scrapy.Field()  # 地区
    title = scrapy.Field()  # 标题
    village = scrapy.Field()  # 地区
    area = scrapy.Field()  # 面积
    type = scrapy.Field()  # 类型
    fenge = scrapy.Field()  # 风格
    ruzhu = scrapy.Field()  # 入住时间
    tese = scrapy.Field()  # 特色
    addr = scrapy.Field()  # 地址
    price = scrapy.Field()  # 价格
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# pm2.5
class SpiderPmItem(scrapy.Item):
    _id = scrapy.Field()
    date = scrapy.Field()  # 时间
    ranking = scrapy.Field()  # 排名
    state = scrapy.Field()  # 状况
    city = scrapy.Field()  # 城市
    province = scrapy.Field()  # 省份
    AQI = scrapy.Field()  # aqi
    chroma = scrapy.Field()  # pm2.5浓度
    pass
