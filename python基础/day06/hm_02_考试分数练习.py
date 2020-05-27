"""
80 以上优秀，60 以上及格，30 以上不及格，30 以下太差
"""

scort = 90

if 60 <= scort < 80:
    print("考试及格")
elif 30 <= scort < 60:
    print("不及格")
elif scort > 80 or scort == 80:
    print("优秀")
else:
    print("太差")