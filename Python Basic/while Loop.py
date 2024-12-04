print("请输入要计算平均值的值：(输入下一个回车，结束输出q)")

value = 0
sum_result = 0
count = 0
mean_value = 0

while value != "q":
    sum_result = sum_result + float(value)
    count += 1
    value = input("请输入：")
if count == 1:
    mean_value == 0
else:
    mean_value = sum_result / (count - 1)
print("平均值为：" + str(mean_value))
