##导入math库
import math

## 加减乘除
a = 1 + 2 - 3 * 4 / 5
print(a)

## 运算顺序 1.() 2.乘方** 3.* / 4.+ -

## 一元二次求根
a = -1
b = -2
c = 3
print((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a))
print((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a))
