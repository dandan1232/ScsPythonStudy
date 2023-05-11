# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 14:10
# @Author  : Lindand
# @File    : Doc10_7.py
# @Description :
# 现有电话簿TelephoneBook.txt和电子邮件簿EmailBook.txt，
# 编写程序，将两个文件合并成一个完整的地址簿AddressBook.txt，
# 要求：如果同一人既有电话又有电子邮件，则要合并成一条信息；如果有人只有电话没有电子邮件，则其电子邮件信息用“------”填充；
# 如果有人只有电子邮件没有电话，则其电话信息用“------”填充。

# 读取电话簿
telephone_book = {}
with open('date/TelephoneBook.txt', 'r', encoding="utf-8") as f:
    for line in f:
        name, phone = line.strip().split()
        telephone_book[name] = phone

# 读取电子邮件簿
email_book = {}
with open('date/EmailBook.txt', 'r', encoding="utf-8") as f:
    for line in f:
        name, email = line.strip().split()
        email_book[name] = email

# 合并地址簿
address_book = {}
for name in set(telephone_book) | set(email_book):
    phone = telephone_book.get(name, '------')
    email = email_book.get(name, '------')
    address_book[name] = (phone, email)

# 输出到文件
with open('date/AddressBook.txt', 'w', encoding="utf-8") as f:
    for name, (phone, email) in address_book.items():
        f.write(f"{name} {phone} {email}\n")
