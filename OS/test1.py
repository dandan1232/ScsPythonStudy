# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 14:18
# @Author  : Lindand
# @File    : test1.py
# @Description :
memory = [0] * 9000  # 声明一个长度为9000的列表，代表内存中的每个点点
free_blocks = []  # 保存所有空闲块的起始地址和长度

while True:
    command = input("请输入命令（格式：a + 100KB）：")
    if command == "exit":
        break

    try:
        process_id, size_str = command.split(" + ")
        if size_str[-2:] != "KB":
            raise ValueError("命令格式错误！")

        size = int(size_str[:-2])  # 获取进程大小（单位：KB）
        if size <= 0:
            raise ValueError("进程大小必须大于0！")

        if process_id.isalpha() and len(process_id) == 1:
            if "+" in command:
                # 分配内存
                allocated = False
                for i in range(len(memory) - size):
                    if memory[i:i + size] == [0] * size:
                        # 可以分配
                        memory[i:i + size] = [1] * size
                        print(f"成功分配 {size}KB 内存给进程 {process_id}，起始地址为 {i // 2}。")
                        allocated = True
                        break

                if not allocated:
                    print(f"分配内存给进程 {process_id} 失败，内存不足！")
            elif "-" in command:
                # 释放内存
                start = int(size_str[:-2]) * 2
                end = start + int(size_str[:-2]) * 1024 // 2
                for i in range(start, end):
                    memory[i] = 0
                print(f"成功释放进程 {process_id} 占用的内存。")

                # 检查是否可以合并相邻的空闲块
                for i, block in enumerate(free_blocks):
                    if block[0] + block[1] == start:
                        free_blocks[i] = (block[0], block[1] + len(process_id) * 2)
                        break
                    elif start + len(process_id) * 2 == block[0]:
                        free_blocks[i] = (start, block[1] + len(process_id) * 2)
                        break
                else:
                    free_blocks.append((start, len(process_id) * 2))

            else:
                raise ValueError("命令格式错误！")
        else:
            raise ValueError("命令格式错误！")

    except ValueError as e:
        print(str(e))

# 输出所有空闲块
print("空闲块列表：")
for i, block in enumerate(free_blocks):
    print(f"空闲块{i + 1}：起始地址：{block[0] // 2}，长度：{block[1] // 2}KB。")
