## 创建类
# 属性-构造函数（构造方法）
# 方法-函数


## 可爱猫猫对象创建
# class CuteCat:
#     # 构造函数
#     def __init__(self, cat_name, cat_age, cat_color) -> None:
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color

#     def speak(self):
#         print("喵" * self.age)

#     def think(self, content):
#         print(f"小猫{self.name}在思考{content}...")


# cat1 = CuteCat("Elsa", 1.8, "黑色")
# print(f"小猫{cat1.name}的年龄是", cat1.age, f"岁，花色是{cat1.color}")
# cat1.think("现在去抓沙发还是去撕纸箱")


## 定义一个学生类
# 1.属性包括学生姓名、学号、以及语数英三科的成绩
# 2.能够设置学生某科目的成绩
# 3.能够打印出该学生的所有科目成绩
class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades.keys():
            self.grades[course] = grade
        else:
            print("不存在科目")

    def print_grades(self):
        print(f"学生{self.name}(学号：{self.id}的成绩为：)")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")


chen = Student("小陈", 123)
chen.set_grade("语文", 92)
chen.set_grade("数学", 94)

print(chen.name)
chen.print_grades()

zeng = Student("小曾", 456)
zeng.set_grade("数学", 95)
print(zeng.grades)
