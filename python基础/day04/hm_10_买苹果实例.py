"""
输入苹果单价，重量计算应付的金额
"""

price = int(input("请输入苹果单价："))
weight = float(input("请输入苹果重量："))
money = price * weight

# print函数输出字符串，数字拼接用 "，"
print("需要支付：", money)
