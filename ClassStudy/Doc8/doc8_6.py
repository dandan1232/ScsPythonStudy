# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:52
# @Author  : Lindand
# @File    : doc8_6.py
# @Description :
# 汉诺（Hanoi）塔问题：有三根柱子A、B、C，A上堆放了3个盘子，盘子大小不等，小盘在上，大盘在下，
# 如图所示。现在要求把这3个盘子从A搬到C，在搬动过程中可以借助B作为中转，每次只允许搬动一个盘子，且在移动过程中在3根柱子上都保持小盘在上，大盘在下。
# 要求基于递归算法的实现，打印出移动的步骤。

def hanoi(n, a, b, c):
    """
    将 n 个盘子从 a 经过 b 移动到 c
    """
    if n == 1:
        print("移动盘子", n, "从", a, "到", c)
    else:
        hanoi(n - 1, a, c, b)
        print("移动盘子", n, "从", a, "到", c)
        hanoi(n - 1, b, a, c)


# 测试
hanoi(3, 'A', 'B', 'C')
