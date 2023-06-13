# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:49
# @Author  : Lindand
# @File    : doc4_2.py
# @Description :在程序中创建两个字典，找出并显示两个字典中相同的键。


dic1 = {'a': 1, 'c': 2, 'd': 3, 'e': 7}
dic2 = {'r': 1, 'g': 2, 'a': 3, 'c': 7}
for i in dic1.keys():
    for j in dic2.keys():
        if i == j:
            print(i)
