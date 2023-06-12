# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 23:21
# @Author  : Lindand
# @File    : doc2_5.py
# @Description :
# 给定字符串，将其中的单词倒序输出。（提示：split到列表）
# 例：给定"What a wonderful day!"，输出："day! wonderful a What"


s=input("一串：")
s1=s.split(" ")
s1.reverse()
str1=" ".join(s1)
print(str1)