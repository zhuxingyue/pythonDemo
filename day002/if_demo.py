'''
    判断一个数是否大于:100
    小于0
    是否在80-100之间
'''
number = int(input("please input a number:"))
if number > 100:
    print("输入的数大于100")
elif number <= 100 and number >= 80:
    print("这个数在80到100中间")
elif number < 0:
    print("这个数据小于0")
else:
    print("这个数在0到80之间")


'''
    需求:
        1.输入一个季度1-4,输出这个季度中有哪些月份,如果不再季度数字给出提示输入错误
        2.输入一个月份输出是那个季度,如果输入月份错误提示
'''

# first question
num = int(input("please input a num:"))
if num == 1:
    print("1月,2月,3月")
elif num == 2:
    print("4th,5th,6th")
elif num == 3:
    print("7th,8th,9th")
elif num ==4:
    print("10th,11th,12th")
else:
    print("erro!!")

# seconde question
num = int(input("please input a month:"))
if num <= 3:
    print("this is 1th")
elif num > 3 and num <= 6:
    print("this is 2th")
elif num > 6 and num <= 9:
    print("this is 3th")
elif num >9 and num <= 12:
    print("this is 4th")
else:
    print("erro !!!")





