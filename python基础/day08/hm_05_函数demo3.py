def printLine(char, times):
    print(char * times)


def printLines(char, times):
    """打印多行分割线

    :param char: 分割线样式字符
    :param times: 分割线个数
    """
    row = 0
    while row < 5:
        printLine(char, times)
        row += 1


printLines("_", 20)
