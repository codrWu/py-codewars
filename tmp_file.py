# -*- coding: utf-8 -*-
"""
文件描述
Created on 2018/7/4
@author: codrwu
"""
__author__ = 'codrwu'


def comp(array1, array2):
    # your code
    if array1 == None or array2 == None:
        return False
    else:
        array1_squared = [x*x for x in array1]
        for x in array2:
            if x not in array1_squared:
                return False
        return True

#print(likes(['Alex', 'Jacob', 'Mark', 'Max']))