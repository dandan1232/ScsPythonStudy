# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 18:56
# @Author  : Lindand
# @File    : doc3_7.py
# @Description :
# 编写程序让用户输入两个字符串（一定是小写字母组成），判断两个字符串是否同构。
# 如果有两个字符串，其中一个字符串的字符重新排列后，能变成另一个字符串，那么称为同构
import collections

num1 = input("一个字符串：")
num2 = input("第二个字符串：")

a = collections.Counter(num1)
b = collections.Counter(num2)

c = set(num1)
d = set(num2)

if a == b and c == d and 'a' <= num1 <= 'z' and 'a' <= num2 <= 'z':
    print("同")

else:
    print("0")
