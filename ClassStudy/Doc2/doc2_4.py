# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:48
# @Author  : Lindand
# @File    : doc2_4.py
# @Description :
# 写一个程序，用户输入一个字符串s，返回一个由s的前2个字符和后2个字符组成的新字符串。如果s的长度小于2，则返回空字符串。
# 例：输入'python'，返回'pyon'。
def get_new_string(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

s = input('请输入一个字符串：')
new_string = get_new_string(s)
print(new_string)

