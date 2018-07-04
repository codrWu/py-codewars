# -*- coding: utf-8 -*-
"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
return the middle character. If the word's length is even, return the middle 2 characters.

获取字符串中间的字符，字符串长度为奇数返回中间一个字符，长度为偶数返回中间两个字符
Created on 2018/7/4
@author: codrwu
"""

__author__ = 'codrwu'
import math
# my function
def get_middle_my(s):
    before_index = math.floor(len(s)/2)
    after_index = math.ceil(len(s)/2)
    if before_index == after_index:
        before_index = before_index - 1
        after_index = after_index -1
    print('%s:%s' % (before_index, after_index))
    result = s[before_index:after_index]
    return result


# Best Practices
def get_middle(s):
    return s[math.floor((len(s)-1)/2):math.floor(len(s)/2)+1]


print(get_middle("test"))