# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 13:34
# @Author  : Lindand
# @File    : doc4_1.py
# @Description :
# 从键盘上随机输入若干个大写英文字母，编写程序使用字典统计所输入的每个字母出现的次数。


Str = input("请输入一串字符:")
resoult = {}  # 定义一个空字典
for i in Str:  # 遍历输入的字符串，以键值对的方式存储在字典中
    resoult[i] = Str.count(i)
for key in resoult:  # 遍历字典，格式化输出结果
    print(f'"{key}":{resoult[key]}次')
