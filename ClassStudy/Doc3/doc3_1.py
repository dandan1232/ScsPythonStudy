# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 13:33
# @Author  : Lindand
# @File    : doc3_1.py
# @Description :
# 求无序整数列表的中位数。如列表元素为偶数个，则取列表升序排列时中间两数中数值较小的元素为中位数。

# median()函数接收一个整数列表作为参数
def median(nums):
    # 使用sorted()函数将列表进行升序排序，然后根据列表长度的奇偶性来计算中位数,
    # 如果列表长度为奇数，中位数就是排序后的中间元素；如果列表长度为偶数，则取中间两个数的平均值，或者是中间两个数中数值较小的那个。
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


# 示例
nums = [1, 2, 5, 4, 3]
print(median(nums))  # 输出 3

nums = [1, 2, 4, 5, 3, 6]
print(median(nums))  # 输出 3.5
