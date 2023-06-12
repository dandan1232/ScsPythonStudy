# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 23:11
# @Author  : Lindand
# @File    : doc2_4.py
# @Description :
# 写一个程序，用户输入一个字符串s，返回一个由s的前2个字符和后2个字符组成的新字符串。如果s的长度小于2，则返回空字符串。
# # 例：输入'python'，返回'pyon'。

s = input(":")
if len(s) < 2:
    print(" ")
else:
    a = s[0:2]
    b = s[len(s) - 2:len(s)]
    c = a + b
    print(c)
