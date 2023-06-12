# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 0:33
# @Author  : Lindand
# @File    : doc3_3.py
# @Description :现有列表[35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]，请编写程序将其中重复的元素去除，并按从小到大的顺序排列后输出。

'''牛'''

data = [35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]

after_date = sorted(list(set(data)))
print(after_date)
