# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 23:31
# @Author  : Lindand
# @File    : doc2_6.py
# @Description :写一个程序处理用户输入的字符串，并按用户要求删除其中第n个字符，返回删除字符后的字符串。


s = input(":")
n = int(input("n:"))
if n > len(s):
    print("超出范围")
elif n==len(s):
    new_s = s[:n-1]
    print(new_s)
else:
    new_s = s[:n-1] + s[n:]
    print(new_s)
