# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 13:58
# @Author  : Lindand
# @File    : doc4_3.py
# @Description :
# 在程序中创建两个字典，找出并显示两个字典中具有相同值（要求数据类型也相同）的键

# 创建两个字典
dict1 = {'a': 1, 'b': 2, 'c': 3, 'lin': "lin"}
dict2 = {'d': 3, 'e': 2, 'f': 1, 'dan': "lin"}

# 初始化一个空列表，用于存储相同值的键
common_keys = []

# 遍历字典1中的键值对
for key1, value1 in dict1.items():
    # 遍历字典2中的键值对
    for key2, value2 in dict2.items():
        # 如果两个字典中具有相同的值
        if value1 == value2:
            # 将该键添加到相同值的键列表中
            common_keys.append(key1)
            common_keys.append(key2)

# 去重并打印结果
print(set(common_keys))
