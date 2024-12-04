## 逻辑运算
# 逻辑运算符号 and or not - 与（并且） 或（或者） 非（不）
# 运算优先级： 1.() 2.not 3.and 4.or

user_age = float(input("请输入您的年龄:"))
user_weight = float(input("请输入您的体重(单位:kg):"))
user_height = float(input("请输入您的体身高(单位:m):"))
user_BMI = user_weight / user_height**2
print("您的年龄为:", str(user_age))
print("您的BMI值为:", str(user_BMI))

if 18 <= user_age <= 25 and 18.5 < user_BMI <= 25:
    print("您是一个正常青年人")
