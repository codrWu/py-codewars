# -*- coding: utf-8 -*-
"""
计算人口在哪一年会超过p
Created on 2018/7/4
@url: https://www.codewars.com/kata/growth-of-a-population/train/python
@author: codrwu
"""
__author__ = 'codrwu'

# my function
def my_nb_year(p0, percent, aug, p):
    year = 0
    while True:
        if p0 >= p:
            return year
        year += 1
        p0 = p0 * (1 + percent / 100) + aug

# the best practice

def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = p0 * (1 + percent / 100) + aug
        year += 1
    return year

print(nb_year(1500, 5, 100, 5000))
