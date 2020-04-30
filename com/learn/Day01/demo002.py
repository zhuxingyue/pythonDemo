'''
python：语句判断
题目：
    判断学习分数：80以上优秀，60分以上及格，30分以上不及格，30分一下差份
'''

learnSort = 20

if learnSort >= 80:
    print("优秀！！")
elif 60 <= learnSort < 80:
    print("及格！！！")
elif 30 <= learnSort < 60:
    print("不及格！！！")
else:
    print("太差！！！")
