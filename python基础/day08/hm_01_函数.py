"""
函数：具有独立功能的代码块，组织成一个小模块；在需要的时候调用

python的函数文档注视放在函数定名名称下面
"""


def multipleTable():
    """打印99乘法表"""
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d\t" % (col, row, (col * row)), end="")
            col += 1
        print("")
        row += 1
