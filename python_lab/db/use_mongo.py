#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    module description
    date: 2019/11/16
    学习mongo数据库
'''

import pymongo

__author__ = "Bigcard"
__copyright__ = "Copyright 2018-2019"

def test1():
    client = pymongo.MongoClient()
    dblist = client.list_database_names()
    for db_name in dblist:
        print(f"数据库名字：{db_name}")


if __name__ == '__main__':
    test1()