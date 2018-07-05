# -*- coding: utf-8 -*-
"""
文件描述
Created on 2018/7/5
@author: codrwu
"""
__author__ = 'codrwu'


'''
知识点：
1.''.join([]) list的元素必须是str类型的
'''
def square_digits(num):
    return int(''.join([str(int(x) * int(x)) for x in str(num)]))


print(square_digits(9119))