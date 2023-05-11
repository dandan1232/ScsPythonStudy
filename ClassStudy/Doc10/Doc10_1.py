# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 13:38
# @Author  : Lindand
# @File    : Doc10_1.py
# @Description :
# 当前路径下有一个文本文件names.txt，包含了按照字典序排序的名字。编写一个程序，当用户自己给定一个名字，按照字典序将其插入到正确的位置。
# 如果这个名字已经存在于文件中，则不要插入。
# 例如：
# Names.txt文件中有如下文本（每个名字占一行）
# Aaron
# Cornell
# 用户输入的待插入文本是：Abbott
# 则生成的新文件夹new_names.txt的内容是：
# Aaron
# Abbott
# Cornell

# 读取names.txt文件中的内容
with open('date/names.txt', 'r') as f:
    names = f.read().splitlines()

# 让用户输入待插入的名字
new_name = input('请输入待插入的名字：')

# 如果这个名字已经存在于列表中，则不需要插入
if new_name in names:
    print('这个名字已经存在于文件中。')
else:
    # 找到新名字应该插入的位置
    index = 0
    while index < len(names) and new_name > names[index]:
        index += 1
    # 插入新名字
    names.insert(index, new_name)
    print('新名字已经成功插入到文件中。')

    # 将更新后的列表写入到new_names.txt文件中
    with open('date/new_names.txt', 'w') as f:
        f.write('\n'.join(names))
