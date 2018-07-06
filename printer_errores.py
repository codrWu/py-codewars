# -*- coding: utf-8 -*-
"""
找出字符串中不是a-m的字符，并输出其数量
Created on 2018/7/5
@url: http://www.codewars.com/kata/printer-errors/python
@author: codrwu
"""

__author__ = 'codrwu'

'''
知识点：
1. [x for x in s if x<'a' or x>'m' 注意有条件判断的写法，只有if要写在for后面，如果有if...else 可以写在前面
'''

def printer_error(s):
    # your code
    return '%s/%s' % (len([x for x in s if x<'a' or x>'m']),len(s))

