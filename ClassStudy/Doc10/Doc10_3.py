# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 13:48
# @Author  : Lindand
# @File    : Doc10_3.py
# @Description :
# 编写程序，提示用户输入一个文件名，读取该文件并统计其中的字符、单词和行的数量，最后打印这些信息。
# 比如文件a.txt中内容如下：
# hello,
# I love you!
# 则字符数为17（字符数包括空格，标点符号等，但是不包括回车换行的符号）
# 单词数目为4. （我们假定标点符号都是跟随着单词后面，不会单独出现）
# 行数为2.
# 让用户输入文件名
filename = input("请输入文件名：")

# 打开文件
with open(filename, "r") as f:
    # 初始化计数器
    char_count = 0
    word_count = 0
    line_count = 0
    # 逐行读取文件中的每一行，对于每一行，分别统计其字符数量、单词数量和行数，然后累加到总的计数器中
    for line in f:
        char_count += len(line)
        word_count += len(line.split())
        line_count += 1

# 关闭文件，并打印出字符数量、单词数量和行数
print("字符数：", char_count)
print("单词数：", word_count)
print("行数：", line_count)
