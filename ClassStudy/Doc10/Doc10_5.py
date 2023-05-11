# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 13:56
# @Author  : Lindand
# @File    : Doc10_5.py
# @Description :
# 伊索寓言英文文件AesopsFalbes.txt，编写程序，读取文件内容，将文本全部转换为小写字符，且将非英文字符都转换为空格，统计其中的高频单词top10，打印输出。

import re
from collections import Counter

# 读取文件内容
with open('date/AesopsFalbes.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 将文本转换为小写字母
text = text.lower()

# 将非英文字符替换为空格
text = re.sub('[^a-zA-Z]', ' ', text)

# 统计单词频率，并输出top10高频单词
word_list = text.split()
word_counts = Counter(word_list)
top10 = word_counts.most_common(10)

print('Top 10 high frequency words:')
for word, count in top10:
    print(f'{word}: {count}')
