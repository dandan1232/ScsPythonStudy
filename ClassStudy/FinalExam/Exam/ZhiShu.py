# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 11:01
# @Author  : Lindand
# @File    : ZhiShu.py
# @Description : 100以内最大的素质

for n in range(100, 1, -1):
    if n % 2 == 0:
        continue
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n)
        break





