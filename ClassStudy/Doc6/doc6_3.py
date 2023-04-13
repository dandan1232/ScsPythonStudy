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

n = int(input("请输入一个整数 n："))

# 输出上半部分
for i in range(n):
    print('  ' * (n - i - 1), end='')  # 输出空格
    print('*   ' * (i + 3))

# 输出下半部分
for i in range(n - 2, -1, -1):
    print('  ' * (n - i - 1), end='')  # 输出空格
    print('*   ' * (i + 3))
