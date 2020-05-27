"""
1。检查有没有车票
2。检查包里有没有危险物品
3。可携带刀的长度是30
"""

hasTicket = True

knifeLength = 30

# if嵌套
if hasTicket:
    print("请进站！！！")
    if knifeLength > 20:
        print("所携带的刀长度是：%d；超过规定的长度" % knifeLength)
    else:
        print("请上车！！")

else:
    print("请先买票！！")