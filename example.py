# coding:utf-8
import os
import datetime
from dao.mongo_web import  MongoWeb

db = MongoWeb(collection = 'leaders')

res = db.find_one_by_date('2018-03-27')

print(res)