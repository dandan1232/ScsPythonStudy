# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:33
# @Author  : Lindand
# @File    : doc8_1.py
# @Description :定义一个lambda函数，返回三个数中的最大值。从键盘输入3个整数，找出其中的最大值。


max_num = lambda a, b, c: max(a, b, c)

a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))

print("三个数中的最大值为：", max_num(a, b, c))
