try:
    user_weight = float(input("请输入您的体重（单位: kg）:"))
    user_height = float(input("请输入你的升高（单位: m）: "))
    user_BMI = user_weight / user_height**2
except ValueError:
    print("输入不为合理的数字，清重新运行程序，并输入正确的数字。")
except ZeroDivisionError:
    print("升高不能为0，清重新运行程序，并输入正确的数字。")
except:
    print("发生了未知错误，请继续")

else:
    print("您的BMI值为：" + str(user_BMI))

finally:
    print("程序结束运行。")
