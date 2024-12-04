import numpy as np

## 字符串 str
# 'hello!'
s = "hello!\n"
# 对字符串求长度
length = len(s)
print("字符串为:", s)
print("字符串长度为:", length)
# 通过索引获得单个字符
print("字符串第一个字符为:", s[0])

## 整数 int
d = -6
print("整数为:", d)

## 浮点数 float
f = 10.07
print("浮点数为:", f)

## 布尔类型 bool
# 真
T = True
# 假
F = False
print(T, F)

## 空值类型 NoneType
# None ≠ 0; None ≠ '' None ≠ False
unknow = None
print("空值为:", unknow)

## 返回数据类型
print(type(s))
print(type(T))
print(type(d))
print(type(unknow))
