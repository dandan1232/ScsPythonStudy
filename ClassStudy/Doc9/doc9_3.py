# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:41
# @Author  : Lindand
# @File    : doc9_3.py
# @Description :
# 当前路径下有文本文件StrInts.txt，该文件中有一段英文文章，在该文章中存在一些整数（有正有负）。
# 编写程序读取该文件、并提取出其中所有的整数，
# 然后将这些整数中偶数位数字上全部都为偶数数字的整数保存到新建的IntsRecord.txt文件中去，保存时每行3个数、每个数占8列、右对齐左补空格。

# 导入chardet库。
import re
import chardet

# 打开文本文件StrInts.txt，读取二进制内容
with open("date/StrInts.txt", "rb") as f:
    data = f.read()

# 使用chardet.detect()函数检测文本文件的编码格式
encoding = chardet.detect(data)["encoding"]

# 根据检测结果，使用相应的编码格式进行读取
text = data.decode(encoding)

# 使用正则表达式匹配整数
pattern = r"-?\d+"
numbers = re.findall(pattern, text)

# 打开新建的IntsRecord.txt文件，写入符合要求的整数
with open("date/IntsRecord.txt", "w") as f:
    count = 0  # 用于计数，每行保存3个数
    for num in numbers:
        even_digits = [int(d) % 2 == 0 for d in num[1::2]]
        if all(even_digits):  # 判断偶数位数字是否都为偶数数字
            f.write(f"{num:>8} ")
            count += 1
            if count == 3:
                f.write("\n")
                count = 0
