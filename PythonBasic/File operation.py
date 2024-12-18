## 文件读取
# f = open("Data\Python Basic\data.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# with open("Data\Python Basic\data.txt", "r", encoding="utf-8") as f:
#     # content = f.read()
#     # print(content)

#     # print(f.readline())
#     # print(f.readline())

#     # print(f.readlines())

#     lines = f.readlines()
#     for line in lines:
#         print(line)

## 文件写入
# 任务1: 在一个新的名字为“poem.txt”的文件里，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高出不胜寒。
with open("Data/Python Basic/poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高出不胜寒。")

# 任务2:在上面的“poem.txt”文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。
with open("Data/Python Basic/poem.txt", "a", encoding="utf-8") as f:

    f.write("\n起舞弄清影，\n何似在人间。")
    # content = f.read()
    # print(content)
