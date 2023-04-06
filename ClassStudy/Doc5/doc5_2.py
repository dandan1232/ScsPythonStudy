# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 13:58
# @Author  : Lindand
# @File    : doc5_2.py
# @Description :
# 从键盘输入三个浮点数a、b和c，求解ax2+bx+c=0的解，并将结果输出到屏幕上。
# 在求解过程中，需要考虑a等于0的无意义情况并给出相应提示信息，同时需要考虑有实数解和无实数解的两种不同的情况。
# （注：当有实数解时不允许使用复数形式来表示结果）。结果（含负数解的实部和虚部）的显示格式要求为：小数部分5列（不含小数点），整个数占10列。

import math

# 获取用户输入的三个浮点数
a = float(input("请输入a："))
b = float(input("请输入b："))
c = float(input("请输入c："))

if a == 0:  # a等于0，无法求解一次项系数为0的一元二次方程
    print("a不能为0，请重新输入。")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:  # 无实数解
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-delta) / (2 * a)
        print("该一元二次方程无实数解，其中两个解的虚部分别为%.5f和-%.5f。" % (imag_part, imag_part))
    elif delta == 0:  # 有一个实数解
        x = -b / (2 * a)
        print("该一元二次方程有一个实数解，解为%.5f。" % x)
    else:  # 有两个实数解
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("该一元二次方程有两个实数解，分别为%.5f和%.5f。" % (x1, x2))
