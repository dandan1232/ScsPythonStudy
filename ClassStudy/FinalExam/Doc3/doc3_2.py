# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 0:28
# @Author  : Lindand
# @File    : doc3_2.py
# @Description :已知一个整数列表，判断列表内容是否为回文，即无论正序还是倒序，列表的内容是否相同。

date = [23, 56, 0, 56, 23]

re_date = date[::-1]  # 倒序

print(re_date)

if date == re_date:
    print("1")
else:
    print("0")
