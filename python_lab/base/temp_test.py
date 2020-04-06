#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    module description
    date: 2020/3/8
'''
__author__ = "Bigcard"
__copyright__ = "Copyright 2018-2020"

import datetime
import time
from tool.printHelper import time_this_function

def test1():
    str = "abvcelsdss"
    print(str[5:-3])

def test2():
    timest = time.strftime("%Y-%m-%d")
    print(timest)
    print(timest.month)
    #now.strftime('%Y-%m-%d %H:%M:%S')
    timest.strftime('%Y-%m-%d')
    print(timest.strftime('%Y-%m-%d'))


def monthdays(y, m):
    oneday = datetime.timedelta(days=1)
    dt0 = datetime.datetime(y, m, 1)
    return filter(lambda dt: dt.month==m,map(lambda n: dt0+n*oneday, range(32)))

def getBetweenDay(begin_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())), "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

@time_this_function
def test3(year,month,day):
    date_list = []
    #begin_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    begin_date = datetime.datetime.strftime(datetime.datetime(year, month, day),"%Y-%m-%d")
    #begin_date = datetime.datetime(2020, 2, 1)
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    if year == datetime.date.today().year and month == datetime.date.today().month:
        end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
    else:
        end_date = last_day_of_month(begin_date)
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    print(date_list)

def test4():
    begin_date = datetime.datetime.strftime(datetime.datetime(2020, 2, 1),"%Y-%m-%d")
    print(begin_date)

def last_day_of_month(any_day):
    """
    获取获得一个月中的最后一天
    :param any_day: 任意日期
    :return: string
    """
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def string_format(self):
    paras = {"host":"localhost", "user":"root", "passwd":"root123", "dbname":"stock"}
    str = 'mysql://{user}:{passwd}@{host}/{dbname}?charset=utf8'.format(**paras)
    print(str)

def test5():
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y-%m-%d')
    print(end_dt)
    date_str = "20200403"
    mydate = time.strptime(date_str,'%Y%m%d')
    print(mydate)

if __name__ == '__main__':
    test2()