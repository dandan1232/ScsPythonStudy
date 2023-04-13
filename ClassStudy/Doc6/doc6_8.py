# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 14:18
# @Author  : Lindand
# @File    : doc6_8.py
# @Description :
# 现有 1 元、2 元和 5 元的钱币若干，如果要用这些钱币（假设足够多）去购买售价n元的商品，请问有多少种不同的组合方式。
# 请用户输入n，输出所有的组合方案。

n = int(input("请输入售价 n："))

count = 0
for i in range(0, n // 5 + 1):
    for j in range(0, (n - 5 * i) // 2 + 1):
        k = n - 5 * i - 2 * j
        if k >= 0 and k % 1 == 0:
            count += 1
            print("{}元: {}个1元 + {}个2元 + {}个5元".format(n, k, j, i))

print("共有{}种不同的组合方式。".format(count))
