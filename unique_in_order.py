# -*- coding: utf-8 -*-
"""
文件描述
Created on 2018/7/6
@url: https://www.codewars.com/trainer/python
@author: codrwu
"""
__author__ = 'codrwu'

'''
知识点
1. list in的用法，注意空list的操作
2. or的用法
3. itertools 工具包 groupby()的用法
'''
def my_unique_in_order(iterable):
    array = []
    for x in iterable:
        if len(array)==0 or x != array[-1]:
            array.append(x)
    return array


# best practice
def unique_in_order_1(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r

from itertools import groupby
def unique_in_order_2(iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order_2('ABBCcAD'))