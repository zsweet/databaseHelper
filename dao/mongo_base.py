# coding:utf-8

import pymongo
import configparser
import logging
import g_val
from bson.objectid import ObjectId


class MongoBase(object):
    def __init__(self, collection=None, database=None):
        try:
            self.Option = {"server": "", "password": "", "username": "", "db": "", "port": "", "collection": ""}
            self.__mongo_config()
            connection = pymongo.MongoClient('mongodb://' +
                                             self.Option["username"] + ':' +
                                             self.Option['password'] + '@' +
                                             self.Option['server'] + ":" +
                                             self.Option['port'])
            if database:
                db = connection[database]
            else:
                db = connection[self.Option['db']]
            if collection:
                self.collection = db[collection]
            else:
                self.collection = db[self.Option['collection']]

        except:
            logging.exception("Exception Logged")

    # mongodb配置用config对象读取配置文件
    def __mongo_config(self):
        config = configparser.ConfigParser()
        #print('配置文件路径为：',g_val.db_path)
        config.read(g_val.db_path)
        #print ('g_val加载状态',config.get("db", "MONGODB_SERVER"))

        self.Option['server'] = config.get("db", "MONGODB_SERVER")
        self.Option['port'] = config.get("db", "MONGODB_PORT")
        self.Option['username'] = config.get("db", "MONGODB_USERNAME")
        self.Option['password'] = config.get("db", "MONGODB_PASSWORD")
        self.Option['db'] = config.get("db", "MONGODB_DB")
        self.Option['collection'] = config.get("db", "MONGODB_COLLECTION")

    # 增加记录
    def save(self, dict):
        return self.collection.save(dict)

    # 插入记录
    def insert(self, dict):
        return self.collection.insert_one(dict)

    # 插入多条记录
    def insert_many(self, dict):
        return self.collection.insert_many(dict)

    # 查询所有记录
    def find_all(self):
        qres = self.collection.find()
        return qres

    # 查询记录
    def find(self, query):
        qres = self.collection.find(query)
        return qres

    # 根据日期查询记录
    def find_date(self, begin_time, end_time):
        qres = self.collection.find({'time': {'$gt': begin_time, '$lt': end_time}})
        return qres

    # 移除记录
    def delete_date(self, begin_date, end_date):
        return self.collection.delete_many({'time': {'$gt': begin_date, '$lt': end_date}})

    # 移除记录
    def delete(self, query):
        return self.collection.delete_many(query)

    # 更新记录
    def update(self, query, value):
        return self.collection.update_many(query, {'$set': value})

    # 更新记录(如果没有记录，进行插入)
    def update_insert(self, query, value):
       return  self.collection.update_many(query, {'$set': value}, upsert=True)


if __name__ == '__main__':
    dao = MongoBase()

    qres = dao.find({'solr_flag': 1})

    for info in qres:
        info['solr_flag'] = 0
        dao.update({'_id': info['_id']}, info)