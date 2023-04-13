# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 13:39
# @Author  : Lindand
# @File    : doc6_3.py
# @Description :
# 用 * 输出一个正六边形。输入一个整数n代表输出的正六边形的边的长度(*的数目)，例如输入n = 3，输出：
# *   *   *
# *   *   *   *
# *   *   *   *   *
# *   *   *   *
# *   *   *
n = int(input("请输入正六边形的边长："))

# 计算正六边形的中心点位置
center = n - 1

for i in range(2 * n - 1):
    line = ""
    if i <= center:
        # 上半部分
        line += " " * (center - i)
        line += "* " * (n + i)
    else:
        # 下半部分
        line += " " * (i - center-1)
        line += "* " * (3 * n - i - 2)
    print(line)

