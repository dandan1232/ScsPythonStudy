# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:14
# @Author  : Lindand
# @File    : doc4_1.py
# @Description :从键盘上随机输入若干个大写英文字母，编写程序使用字典统计所输入的每个字母出现的次数。

'''牛'''
apl=input("ABC:")
resoult={}
for i in apl:
    resoult[i]=apl.count(i)
for key in resoult:
    print(f'"{key}":{resoult[key]}次')