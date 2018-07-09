# -*- coding: utf-8 -*-
"""
文件描述
Created on 2018/7/9
@author: codrwu
"""
__author__ = 'codrwu'

def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits_list = []
    index = 4
    while(index < len(bits)):
        bits_list.append(bits[index-4 : index])
        index += 4
    result = ''
    for x in bits_list:
        result = result + x.replace('1111', '-').replace('0000', ' ').replace('1100', '.')
    return result

# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
#
#
# def decodeMorse(morseCode):
#     # ToDo: Accept dots, dashes and spaces, return human-readable message
#     return ' '.join(''.join(x for x in word) for word in morseCode.split('   '))
#
#
# print(decodeMorse('···· · −·−− ·−−− ··− −·· ·'))
print(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))