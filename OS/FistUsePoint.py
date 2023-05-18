# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 14:04
# @Author  : Lindand
# @File    : FistUsePoint.py
# @Description :
memory_size = 9 * 1024  # 9K
memory = [0] * memory_size  # 初始化内存

while True:
    command = input("请输入命令（格式：a + 100KB）：")
    if command == "exit":
        break
    try:
        process_id, size_str = command.split(" + ")
        size = int(size_str[:-2])  # 将字符串单位KB转换为整数字节数
        if process_id.isdigit() or process_id.islower():
            process_id = ord(process_id.upper()) - ord("A")  # 将字母转换为数字编号，从0开始
            if "+" in command:  # 进程进入内存
                # 使用首次适应算法进行内存分配
                start, end = None, None
                for i in range(memory_size):
                    if not memory[i]:
                        if start is None:
                            start = i
                        if i - start + 1 == size:
                            end = i
                            break
                    else:
                        start = None
                if end is not None:
                    for i in range(start, end + 1):
                        memory[i] = 1  # 将已分配的内存标记为已使用
                    print(f"分配成功，进程{process_id}从{start}开始，共占用{size}字节")
                else:
                    print(f"内存不足，无法分配进程{process_id}")
            elif "-" in command:  # 进程离开内存
                start = None
                for i in range(memory_size):
                    if memory[i] == process_id:
                        if start is None:
                            start = i
                        memory[i] = 0  # 将已释放的内存标记为未使用
                if start is not None:
                    print(f"释放成功，进程{process_id}从{start}开始，共释放{size}字节")
                else:
                    print(f"进程{process_id}不存在于内存中")
            else:
                print("无效命令")
        else:
            print("无效进程编号")
    except ValueError:
        print("无效命令")

# 输出所有外部碎块
start, end = None, None
for i in range(memory_size):
    if not memory[i]:
        if start is None:
            start = i
    else:
        if start is not None:
            end = i - 1
            print(f"外部碎块，编号{start}-{end}，共{end - start + 1}字节")
            start, end = None, None
if start is not None:
    end = memory_size - 1
    print(f"外部碎块，编号{start}-{end}，共{end - start + 1}字节")
