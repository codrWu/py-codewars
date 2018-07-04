# -*- coding: utf-8 -*-
"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

找出list出现奇数次的数字(符合条件的数字只有一个)
Created on 2018/7/4
@author: codrwu
"""
__author__ = 'codrwu'

'''
知识点：
1. dict 遍历方法

2. count 方法
    返回元素在列表中出现的次数
'''


def my_find_it(seq):
    num_dict = {}
    for item in seq:
        if str(item) not in num_dict.keys():
            num_dict[str(item)] = 1
        else:
            num_dict[str(item)] += 1
    print(num_dict)
    for key, value in num_dict.items():
        if value % 2 != 0:
            return int(key)


#the best practice
def find_it(seq):
    for i in seq:
        if seq.count(i)%2 != 0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))