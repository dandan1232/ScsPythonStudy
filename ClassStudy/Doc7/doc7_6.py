# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:46
# @Author  : Lindand
# @File    : doc7_6.py
# @Description :给定如下一段英文
# A major drawback of cross-network recommender solutions is that they can only be applied to users that are overlapped across networks.
# Thus, the non-overlapped users, which form the majority of users are ignored.
# As a solution, we propose CnGAN, a novel multi-task learning based recommend architecture.
# 编写一个函数，要求实现以下功能：
# 1）统计有多少个不同的单词；
# 2）根据每个单词ASCII码值的和（单词they ASCII码值的和是：116+104+101+121=442）对单词进行从小到大的排序，重复出现的单词只算一次的和，按行输出单词及对应的和。

def word_count_and_sort(text):
    # 统计单词出现次数
    word_count = {}
    words = text.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # 统计不同单词的数量
    distinct_words = len(word_count)

    # 对单词按ASCII码值和排序
    word_sum = {}
    for word in word_count:
        word_ascii_sum = sum(ord(char) for char in word)
        if word_ascii_sum not in word_sum:
            word_sum[word_ascii_sum] = [word]
        else:
            word_sum[word_ascii_sum].append(word)

    # 按ASCII码值和输出单词
    for ascii_sum in sorted(word_sum):
        for word in word_sum[ascii_sum]:
            count = word_count[word]
            print(f"{word}: {ascii_sum * count}")

    return distinct_words


text = "A major drawback of cross-network recommender solutions is that they can only be applied to users that are overlapped across networks. " \
       "Thus, the non-overlapped users, which form the majority of users are ignored. " \
       "As a solution, we propose CnGAN, a novel multi-task learning based recommend architecture."
distinct_words = word_count_and_sort(text)
print(f"不同的单词有 {distinct_words}"+"个")
