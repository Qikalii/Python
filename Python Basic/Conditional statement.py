## if条件语句
# 条件：布尔值 Ture False
# 比较预算符：== != > >= < <=
# Python根据缩进分块 一般是4个空格为一个空格

mood_index = int(input("对象今天的心情指数是："))
if mood_index >= 60:
    print("恭喜！尽情去打游戏吧！")
else:  # mood_index < 60
    print("还是别打了吧。")

## 嵌套多条件判断
# BMI = 体重 / （身高 ** 2）
user_weight = float(input("请输入您的体重(单位:kg):"))
user_height = float(input("请输入您的体身高(单位:m):"))
user_BMI = user_weight / user_height**2
print("您的BMI值为:", str(user_BMI))
# 偏瘦:user_BMI <= 18.5
# 正常:18.5 < user_BMI <= 25
# 偏胖:25 < user_BMI <= 30
# 肥胖:30 < user_BMI
if user_BMI <= 18.5:
    print("此MBI值属于偏瘦范围。")
elif 18.5 < user_BMI <= 25:
    print("此MBI值属于正常范围。")
elif 25 < user_BMI <= 30:
    print("此MBI值属于偏胖范围。")
else:
    print("此MBI值属于肥胖范围。")
