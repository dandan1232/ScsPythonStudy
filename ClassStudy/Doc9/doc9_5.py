# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:42
# @Author  : Lindand
# @File    : doc9_5.py
# @Description :
# 当前路径下有文本文件numbers.txt，文件中的每一行都是一个浮点数，编写程序读取出所有的浮点数。要求：
# a)	从小到大排序，将排序后的结果写到当前路径下新生成的一个文本文件sort.txt中，每个数占一行。
# b)	求出这些数字的均值、方差，将结果追加到上述文件sort.txt中，每个数占一行。

import numpy as np

# 读取所有浮点数
with open('date/numbers.txt', 'r') as f:
    numbers = [float(line.strip()) for line in f]

# 从小到大排序
numbers.sort()

# 写入排序后的结果到sort.txt文件中
with open('date/sort.txt', 'w') as f:
    for number in numbers:
        f.write('{}\n'.format(number))

# 计算均值和方差
mean = np.mean(numbers)
var = np.var(numbers)

# 追加均值和方差到sort.txt文件中
with open('date/sort.txt', 'a') as f:
    f.write('{}\n{}\n'.format(mean, var))

print('排序和统计完成')
