# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 11:48
# @Author  : Lindand
# @File    : InputZhishu.py
# @Description :输入一个数字判断是不是素数


num = int(input("num:"))

for i in range(2, num):
    if num % i == 0:
        print("0")
else:
    print("1")
