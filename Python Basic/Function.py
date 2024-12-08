## 计算扇形面积
def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius**2
    return sector_area


area = calculate_sector(60, 5)
print(("面积为:{area}").format(area=area))
print("面积为:", area)
print(f"面积为:{area}")


## 计算BMI的函数，函数名为calculate_BMI
# 1.可以计算在任意体重和升高的的BMI值
# 2.执行过程中打印一句话，“您的BMI的分类为：xx”
"""
偏瘦:user_BMI <= 18.5
正常:18.5 < user_BMI <= 25
偏胖:25 < user_BMI <= 30
肥胖:30 < user_BMI
"""
# 3.返回计算的出的BMI值


def calculate_BMI(user_weight, user_height):
    user_BMI = user_weight / user_height**2
    if user_BMI <= 18.5:
        print("此MBI值属于偏瘦范围。")
    elif 18.5 < user_BMI <= 25:
        print("此MBI值属于正常范围。")
    elif 25 < user_BMI <= 30:
        print("此MBI值属于偏胖范围。")
    else:
        print("此MBI值属于肥胖范围。")
    return user_BMI


user_weight = float(input("请输入您的体重(单位:kg):"))
user_height = float(input("请输入您的体身高(单位:m):"))

user_BMI = calculate_BMI(user_weight, user_height)
