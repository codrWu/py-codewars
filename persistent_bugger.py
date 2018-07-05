# -*- coding: utf-8 -*-
"""
文件描述
Created on 2018/7/5
@author: codrwu
"""
__author__ = 'codrwu'
'''
知识点:
1. reduce 用法
2. 递归调用
'''


from functools import reduce
def f(x, y):
    return int(x)*int(y)
# my function
def my_persistence(n):
    times = 0
    while len(str(n)) > 1:
        n = reduce(f, str(n))
        times += 1
    return times

# the best prectice
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1

