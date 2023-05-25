# -*- coding: utf-8 -*-
# @Time    : 2023/5/25 13:54
# @Author  : Lindand
# @File    : doc12_3.py
# @Description :
# 为学校人事部门设计一个简单的人事管理程序，满足如下要求：
# （1）学校人员分为三类：教师、学生、职员；
# （2）三类人员的共同属性是姓名、性别、年龄、部门；
# （3）教师的特别属性是职称、主讲课程；
# （4）学生的特别属性是专业、入学日期；
# （5）职员的特别属性是工资。
# 建议使用继承提升代码复用度，使用类属性统计学校总人数和各类人员的人数，能够随着新人进入注册和离校注销而动态变化。

class Person:
    total_count = 0

    def __init__(self, name, gender, age, department):
        self.name = name
        self.gender = gender
        self.age = age
        self.department = department
        Person.total_count += 1

    def __del__(self):
        Person.total_count -= 1


class Teacher(Person):
    teacher_count = 0

    def __init__(self, name, gender, age, department, title, course):
        super().__init__(name, gender, age, department)
        self.title = title
        self.course = course
        Teacher.teacher_count += 1

    def __del__(self):
        super().__del__()
        Teacher.teacher_count -= 1


class Student(Person):
    student_count = 0

    def __init__(self, name, gender, age, department, major, enrollment_date):
        super().__init__(name, gender, age, department)
        self.major = major
        self.enrollment_date = enrollment_date
        Student.student_count += 1

    def __del__(self):
        super().__del__()
        Student.student_count -= 1


class Staff(Person):
    staff_count = 0

    def __init__(self, name, gender, age, department, salary):
        super().__init__(name, gender, age, department)
        self.salary = salary
        Staff.staff_count += 1

    def __del__(self):
        super().__del__()
        Staff.staff_count -= 1


# 示例用法
# 创建教师对象
teacher1 = Teacher("张老师", "男", 40, "数学", "副教授", "线性代数")
teacher2 = Teacher("王老师", "女", 35, "化学", "教授", "量子力学")

# 创建学生对象
student1 = Student("林同学", "女", 20, "计算机", "软件工程", "2022-09-01")
student2 = Student("徐同学", "女", 21, "物理", "物理学", "2021-08-25")

# 创建职员对象
staff1 = Staff("花工", "女", 30, "学生公寓", 50000)
staff2 = Staff("钱工", "男", 45, "图书馆", 45000)

# 打印总人数和各类人员的人数
print("总人数:", Person.total_count)
print("教师人数:", Teacher.teacher_count)
print("学生人数:", Student.student_count)
print("职员人数:", Staff.staff_count)

# 注销一个教师
del teacher2

# 打印总人数和各类人员的人数
print("总人数:", Person.total_count)
print("教师人数:", Teacher.teacher_count)
print("学生人数:", Student.student_count)
print("职员人数:", Staff.staff_count)

'''在上述代码中，定义了Person类作为父类，用于表示学校人员的共同属性。Teacher、Student和Staff类继承自Person类，并添加了各自特有的属性。
每个类都有一个类属性total_count用于统计总人数，并在对象创建和销毁时进行更新。每个子类也有自己的类属性，如teacher_count、student_count和staff_count，用于统计各类人员的人数。
在每个类的构造方法中，使用super().__init__()调用父类的构造方法来初始化共同属性。然后，在子类的构造方法中添加特定的属性。
在每个类的析构方法__del__()中，使用super().__del__()调用父类的析构方法，并更新相应的类属性以反映对象的销毁。'''
