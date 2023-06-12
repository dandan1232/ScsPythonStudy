# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 0:03
# @Author  : Lindand
# @File    : doc3_1.py
# @Description :求无序整数列表的中位数。如列表元素为偶数个，则取列表升序排列时中间两数中数值较小的元素为中位数。
'''元祖找位置直接用切片，[]这样的'''
num = input(":").split(" ")
num = [int(i) for i in num]
num1 = sorted(num, reverse=False)
print(num1)
# print(num1[2])
if len(num1) % 2 != 0:
    mediu = num1[len(num1) // 2]
    print(mediu)
else:
    mediu1 = num1[len(num1) // 2]
    mediu2 = num1[len(num1) // 2 - 1]
    if mediu1 < mediu2:
        print(mediu1)
    else:
        print(mediu2)
