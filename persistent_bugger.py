# -*- coding: utf-8 -*-
"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
 which is the number of times you must multiply the digits in num until you reach a single digit.

 一个数字的各位数字的乘积最后为一位数字，返回计算次数
Created on 2018/7/5
@url: http://www.codewars.com/kata/persistent-bugger/python
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

