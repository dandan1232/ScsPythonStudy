# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 14:50
# @Author  : Lindand
# @File    : doc4_7.py
# @Description :
# 使用random模块生成一个整数类型的随机数集合：从5到9(包括9)中随机选择一个整数x，生成1到x+1个[0,50]范围内的随机数，这些数字组成集合A。
# 同理，按此方法生成集合B。在此基础上实现以下功能：
# a)	显示A和B的结果；
# b)	要求用户输入 A | B 和 A & B 的结果，并告诉用户其答案是否正确。如果用户回答错误，程序将正确结果打印出来。

import random

# 生成集合A
x = random.randint(5, 9)
A = set(random.randint(0, 50) for i in range(random.randint(1, x + 1)))

# 生成集合B
y = random.randint(5, 9)
B = set(random.randint(0, 50) for i in range(random.randint(1, y + 1)))

# 显示集合A和集合B的结果
print("集合A：", A)
print("集合B：", B)

# 要求用户输入 A | B 和 A & B 的结果，并告诉用户其答案是否正确
union_ans = input("请计算 A | B：")
if set(map(int, union_ans.split())) == A.union(B):
    print("回答正确！")
else:
    print("回答错误！正确答案是：", A.union(B))

intersect_ans = input("请计算 A & B：")
if set(map(int, intersect_ans.split())) == A.intersection(B):
    print("回答正确！")
else:
    print("回答错误！正确答案是：", A.intersection(B))
