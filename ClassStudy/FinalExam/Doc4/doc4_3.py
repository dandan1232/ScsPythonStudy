# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:52
# @Author  : Lindand
# @File    : doc4_3.py
# @Description :在程序中创建两个字典，找出并显示两个字典中具有相同值（要求数据类型也相同）的键

dic1 = {'a': '1', 'c': 'h', 'd': 3, 'e': 7}
dic2 = {'r': 1, 'g': 'h', 'a': 9, 'c': 7}
for i in dic1.values():
    for j in dic2.values():
        if i == j and type(i) == type(j):
            print(i, end=" ")
