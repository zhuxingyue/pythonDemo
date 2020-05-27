'''
python 中的枚举：
    利用户enumerate函数创建枚举
    enumerate()
'''

# 创建枚举"abc"为序列，枚举初始值
enum = enumerate("abc", 2)
print(list(enum))

#   创建枚举元素列表
lis = ["upper", "drop", "right", "left"]
# 生成枚举对象enum1
enum1 = enumerate(lis, 4)
# print(list(enum1))

# 遍历枚举对象，取出枚举中的元素
for i, item in enum1:
    print(i, "  ", item)

print()
