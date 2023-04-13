# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 14:17
# @Author  : Lindand
# @File    : doc6_7.py
# @Description :
# 从键盘输入一个十进制正整数，利用列表和除二取余法，计算出该数字的二进制值。
decimal = int(input("请输入一个十进制正整数："))

binary = []
while decimal > 0:
    remainder = decimal % 2  # 取余数
    binary.append(remainder)  # 将余数添加到二进制列表中
    decimal //= 2  # 整除二

binary.reverse()  # 翻转列表，得到正确的二进制值

print("该数字的二进制值为：", end="")
for bit in binary:
    print(bit, end="")
