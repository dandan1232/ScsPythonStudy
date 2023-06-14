# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 13:33
# @Author  : Lindand
# @File    : doc6_1.py
# @Description :
# 用 * 输出一个等腰三角形。提示用户输入一个整数n，代表输出的等腰三角形由n行 * 组成。例：输入n = 3。输出：
#   *
#  ***
# *****

n = int(input("请输入一个整数n："))

# 输出等腰三角形
for i in range(1, n + 1):
    # 打印每一行的空格
    for j in range(1, n - i + 3):
        print("_", end="")
    # 打印每一行的星号
    for k in range(1, 2 * i):
        print("*", end="")
    print()  # 换行
