# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 14:40
# @Author  : Lindand
# @File    : doc4_6.py
# @Description :
# 通过[0,500]范围内随机数发生的方法分别创建两个整数数据的集合，要求每个集合中数据的个数分别要超过200个。在此基础上实现：
# a)	求出两个集合中不相同的数据，并进行显示。要求每行显示10条，每个数占5列，右对齐；
# b)	求出两个集合中相同的数据，并进行显示。要求每行显示10条，每个数占5列，右对齐；

import random

# 生成两个超过200个随机整数的集合
set1 = set(random.sample(range(501), 250))
set2 = set(random.sample(range(501), 300))

# 求出两个集合中不相同的数据，并进行显示
diff_set = set1 ^ set2
print("集合1和集合2中不相同的数据：")
for idx, num in enumerate(sorted(diff_set)):
    print(f"{num:>5}", end="")
    if (idx + 1) % 10 == 0:
        print()

# 求出两个集合中相同的数据，并进行显示
common_set = set1 & set2
print("\n集合1和集合2中相同的数据：")
for idx, num in enumerate(sorted(common_set)):
    print(f"{num:>5}", end="")
    if (idx + 1) % 10 == 0:
        print()
