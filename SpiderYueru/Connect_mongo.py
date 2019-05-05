from pymongo import MongoClient

# 建立连接
client = MongoClient('localhost', 27017)

# 连接所需数据库，fangwu为数据库名
db = client.fangwu


# 向集合中写数据
class YurRu(object):
    # 选择所用的集合，也就是我们通常所说的表，test为表名
    collection = db.yueru

    @classmethod
    def insert(cls,item):
        cls.collection.insert( item )
        pass
    pass


class Pm(object):
    # 选择所用的集合，也就是我们通常所说的表，test为表名
    collection = db.pm

    @classmethod
    def insert(cls,item):
        cls.collection.insert( item )
        pass
    pass
# def Insert(item):
#     # 选择所用的集合，也就是我们通常所说的表，test为表名
#     collection = db.yueru
#     if item['tese']:
#         item['tese'] = item['tese'].strip()
#         pass
#     collection.insert( item )
#     pass