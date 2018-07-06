# -*- coding: utf-8 -*-
"""
Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False
depending on if the integer is a prime.

判断质数或素数（只能被1和他本身整除的正整数）
Created on 2018/7/6
@url:https://www.codewars.com/kata/is-a-number-prime/python
@author: codrwu
"""
__author__ = 'codrwu'

'''
知识点：
1. range() 方法使用
2. any() / not any() 用法
'''
def is_prime(num):
    if num < 2:
        return False
    else:
        for x in range(2, num):
            if num % x == 0 and x != num:
                return False
    return True

# the best practice
def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))