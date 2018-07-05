# -*- coding: utf-8 -*-
"""
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays
have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

数组b中的元素是数组a中元素的平方，可以不考虑顺序，但元素必须一一对应，
Created on 2018/7/5
@author: codrwu
"""
__author__ = 'codrwu'
'''
知识点：
1. in, not in 在判断语句中的用法
2. sort() 方法的用法
'''

# 该方法是错的
def my_comp(array1, array2):
    # your code
    if array1 == None or array2 == None:
        return False
    else:
        array1_squared = [x*x for x in array1]
        for x in array2:
            if x not in array1_squared:
                return False
        return True

def comp(array1, array2):
    return None not in (array1, array2) and sorted([x*x for x in array1]) == sorted(array2)


a1 = None
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))