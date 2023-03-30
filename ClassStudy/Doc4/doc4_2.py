# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 13:56
# @Author  : Lindand
# @File    : doc4_2.py
# @Description :在程序中创建两个字典，找出并显示两个字典中相同的键。

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
b = {'b': 2, 'c': 13, 'a': 0}
print(a.keys() & b.keys())
