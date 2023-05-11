# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 13:44
# @Author  : Lindand
# @File    : Doc10_2.py
# @Description :
# 编写程序打开一个文本文件Mary.txt，读取每一行并在每一行的前面加上行号，保存到输出文件中。如果输入文件内容为：
# Mary had a little lamb,
# Whose fleece was white as snow.
# And everywhere that Mary went,
# The lamb was sure to go!
# 那么程序生成的输出文件内容为：
# /* 1 */ Mary had a little lamb,
# /* 2 */ Whose fleece was white as snow.
# /* 3 */ And everywhere that Mary went,
# /* 4 */ The lamb was sure to go!
# 提示用户提供输入文件和输出文件的名字。

# 让用户输入输入文件和输出文件的名字
input_file = input("请输入输入文件的名字：")
output_file = input("请输入输出文件的名字：")

# 打开输入文件和输出文件
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # 使用一个计数器来记录当前行号
    line_num = 1
    # 读取输入文件中的每一行，并在每一行的前面加上行号，将结果写入到输出文件中
    for line in f_in:
        f_out.write("/* " + str(line_num) + " */ " + line)
        line_num += 1

# 关闭输入文件和输出文件
f_in.close()
f_out.close()
