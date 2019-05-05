# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.htm
from .Connect_mongo import YurRu,Pm
import csv


class SpideryueruPipeline(object):
    def process_item(self, item, spider):
        print(item)
        try:
            # with open( 'yueru.csv', 'a+', newline='' ) as f:
            #     writer = csv.writer( f )
            #     writer.writerow( item.values() )
            YurRu.insert(item)
        except Exception as ex:
            print(ex.args)
            pass
        return item
    pass


# 爬取pm2.5
class SpiderpmPipeline(object):
    def process_item(self, item, spider):
        print(item)
        try:
            Pm.insert(item)
        except Exception as ex:
            print(ex.args)
            pass
        return item
