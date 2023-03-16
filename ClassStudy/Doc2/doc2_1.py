# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:29
# @Author  : Lindand
# @File    : doc2_1.py
# @Description :从键盘输入一个3位整数，请编写程序计算三位整数的各位数字之和，并输出到屏幕上，要求输出占4列，右对齐。

num = input("请输入一个3位整数：")  # 从键盘输入一个字符串
sum = int(num[0]) + int(num[1]) + int(num[2])  # 将字符串中的字符转换为整数，并计算各位数字之和
print("各位数字之和为：{:>4d}".format(sum))  # 输出结果，占4列，右对齐
