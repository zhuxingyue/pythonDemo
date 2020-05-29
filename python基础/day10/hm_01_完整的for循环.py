# 完整的for循环;循环结束执行else语句
student_info = [
    {"name": "小美"},
    {"name": "小黄"}
]
name = "李四"
for dic_info in student_info:
    print(dic_info)
    if dic_info["name"] == name:
        print("找到了")
        break
else:
    print("没找到！%s" % name)
print("循环结束！！")
