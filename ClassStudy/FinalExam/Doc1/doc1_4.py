# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 20:47
# @Author  : Lindand
# @File    : doc1_4.py
# @Description :
# 一只大象口渴了，要喝 20 升水才能解渴，但现在只有一个深 h 厘米，底面半径为 r 厘米的小圆桶(h 和 r 都是整数)。
# 问大象至少要喝多少桶水才会解渴。编写程序输入半径和高度，输出需要的桶数（一定是整数）。


r = input("输入半径：")
h = input("输入高度：")
v = 3.14 * int(r) * int(r) * int(h)
num = 20000 // v
print(20000/v)
if (20000 % v != 0):
    print(num + 1)
else:
    print(num)
