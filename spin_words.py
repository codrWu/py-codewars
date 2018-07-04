# -*- coding: utf-8 -*-
"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

一个句子里，如果单词的长度大于5则将该单词倒着拼，其他不变
Created on 2018/7/4
@author: codrwu
"""
__author__ = 'codrwu'

'''
知识点：
1. list 倒序 L[::-1]
2. 列表生成器 [for X in L]，并注意如果有条件判断的写法
'''

# my function
def my_spin_words(sentence):
    # Your code goes here
    words = sentence.split(' ')
    new_sentence = []
    for word in words:
        new_word = ''
        if len(word) >= 5:
            i = -1
            while i >= (-len(word)):
                new_word = new_word + word[i]
                i = i - 1
        else:
            new_word = word
        new_sentence.append(new_word)
    return ' '.join(new_sentence)


def spin_words(sentence):
    return ' '.join(word[::-1] if len(word)> 5 else word for word in sentence.split(' '))


print(spin_words('Welcome'))
