# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:51
# @Author  : Lindand
# @File    : doc8_4.py
# @Description :写一个自定义函数，用于判断两个数是否为幸运数对。
# 所谓幸运数对是指两数相差3，且各位数字之和能被6整除的一对数，如147和150就是幸运数对。要求找出所有的三位数幸运数对。

def is_lucky_pair(a, b):
    if abs(a - b) != 3:
        return False
    if (sum(map(int, str(a))) + sum(map(int, str(b)))) % 6 != 0:
        return False
    return True


lucky_pairs = []
for a in range(100, 1000):
    for b in range(a + 1, 1000):
        if is_lucky_pair(a, b):
            lucky_pairs.append((a, b))

print("三位数幸运数对：", lucky_pairs)
