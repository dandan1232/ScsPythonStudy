# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:42
# @Author  : Lindand
# @File    : doc9_7.py
# @Description :
# 当前路径下有文本文件word.txt中包含了20个英文单词，编写一个程序，删除文件中所有不以元音开头的单词，结果保存在当前路径下新生成的new_word.txt中。

import re

# 定义元音字母的正则表达式
vowel_pattern = re.compile(r'^[aeiouAEIOU]')
# 打开两个文件，分别是原文件和新文件
with open('date/word.txt', 'r') as infile, open('date/new_word.txt', 'w') as outfile:
    # 逐行读取原文件中的内容
    for line in infile:
        # 使用strip()方法去掉行末的换行符
        word = line.strip()
        # 判断单词是否以元音字母开头
        if vowel_pattern.match(word):
            outfile.write(word + '\n')

print('筛选完成')
