# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:31
# @Author  : Lindand
# @File    : doc1_2.py
# @Description :
# 从键盘输入四个整数，并输出其中最大的数。

# a = int(input("请输入第一个整数："))
# b = int(input("请输入第二个整数："))
# c = int(input("请输入第三个整数："))
# d = int(input("请输入第四个整数："))
#
# max_num = a  # 假设a是最大的数
# if b > max_num:
#     max_num = b
# if c > max_num:
#     max_num = c
# if d > max_num:
#     max_num = d
#
# print("最大的数是：", max_num)


print("请输入需要比较的四个值，用空格隔开:")


def getMax(*a):
    m = a[0]
    for x in a:
        if x > m:
            m = x
    return m


s, d, f, e = map(int, input().split())
print("最大值:", max(s, d, f, e))
