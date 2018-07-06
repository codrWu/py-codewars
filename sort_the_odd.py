# -*- coding: utf-8 -*-
"""
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

将数组中的奇数按大小顺序排列，偶数位置不变，0算偶数，空数组返回它本身
Created on 2018/7/6
@url:https://www.codewars.com/kata/sort-the-odd/python
@author: codrwu
"""
__author__ = 'codrwu'


'''
知识点：
1. sorted 排序，reverse参数使用
2. list 的pop()方法
'''

def my_sort_array(source_array):
    # Return a sorted array.
    odd_array = sorted([x for x in source_array if x%2 > 0])
    index = 0
    new_array = []
    for x in source_array:
        if x%2 == 0:
            new_array.append(x)
        else:
            new_array.append(odd_array.pop())
            index += 1
    return new_array


# the best practice
def sort_array(source_array):
    odd_array = sorted([y for y in source_array if y%2 >0], reverse=True)
    return [x if x%2 == 0 else odd_array.pop() for x in source_array]