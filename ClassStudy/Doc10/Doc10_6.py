# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 14:06
# @Author  : Lindand
# @File    : Doc10_6.py
# @Description :
# 当前路径下有一个文件夹folder，文件夹下有多个文本文件file1~file4.txt（文件名称和文件内容都是英文的），
# 将这些文本文件内容合并生成一个新的文本文件merge.txt存放在folder文件夹下新建的new文件夹中，不破坏原始文件。

def main():
    file = lambda x: "date/folder/file" + str(x) + ".txt"
    f2 = "date/folder/merge.txt"

    outfile = open(f2, 'w', encoding='utf-8')
    infile = None
    for i in range(1, 4 + 1):
        infile = open(file(i), 'r')
        for line in infile:
            outfile.write(line)
    print("合并完成!")
    infile.close()
    outfile.close()


main()
