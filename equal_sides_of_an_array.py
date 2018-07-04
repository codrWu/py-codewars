# -*- coding: utf-8 -*-
"""
You are going to be given an array of integers.
Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

返回N，整数list里第N个元素前面所有元素的和等于后面所有元素的和，如果不存在则返回-1
Created on 2018/7/4
@author: codrwu
"""
from functools import reduce

__author__ = 'codrwu'

'''
知识点：
1. reduce() 用法
2. range() 生成list用法
3. sum() 用法
'''


def f(x,y):
    return x+y
def my_find_even_index(arr):
    #your code here
    i = 0
    result = -1
    while i < len(arr):
        sum_before = 0
        if i > 0:
            sum_before = reduce(f, arr[:i])
        sum_after = 0
        if i+1 < len(arr):
            sum_after = reduce(f, arr[i+1:])
        if sum_before == sum_after:
            return i
        i += 1
    return result

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

print(find_even_index([123,123,123]))