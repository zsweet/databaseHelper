# coding:utf-8

import datetime
import os

#这里可以定义变量



if os.name == 'nt':
    #db_path = "F:\\svn\\opinion_new\\news\\db.ini"  # 数据库配置文件  绝对路径
    db_path = "db.ini"  # 数据库配置文件


elif os.name == 'posix':
    db_path = "/root/opinion_new/news/db.ini"
