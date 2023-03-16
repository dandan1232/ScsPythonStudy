# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:50
# @Author  : Lindand
# @File    : doc2_5.py
# @Description :
# 给定字符串，将其中的单词倒序输出。（提示：split到列表）
# 例：给定"What a wonderful day!"，输出："day! wonderful a What"

def reverse_words(s):
    # 使用split函数将字符串按照空格分割成单词列表
    words = s.split()
    # 倒序输出单词列表
    return ' '.join(words[::-1])

s = "What a wonderful day!"
reversed_words = reverse_words(s)
print(reversed_words)
