# range(s,e,step) 整数数列 起始s到结束e,但不包括e,表示步长

## 计算1+...+100
sum_result = 0
for i in range(1, 101, 1):
    sum_result = sum_result + i
print(sum_result)
