# -*- coding: utf-8 -*-
"""
文件描述
Created on 2018/7/4
@author: codrwu
"""
__author__ = 'codrwu'

from functools import reduce
def f(x, y):
    return x*y
print(reduce(f, [1,23,2]))

print('10003' < '22')
#print(likes(['Alex', 'Jacob', 'Mark', 'Max']))