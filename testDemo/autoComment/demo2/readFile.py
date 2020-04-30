import os


class ReadFile():
    # 读取文件内容
    def readFile(self, filePath):
        with open(filePath, 'r') as fp:
            re = fp.read()
            re = re.split("\n")
        return re

    # 获取文件名称
    def getFileName(self, fileDirecter):
        fileNameList = []
        dir = os.path.isdir(fileDirecter)
        if dir:
            files = os.listdir(fileDirecter)
            for file in files:
                fileName = os.path.basename(file)
                fileName = os.path.join(fileDirecter, fileName)
                # print(fileName)
                fileNameList.append(fileName)
        else:
            print("文件目录错误！！！")

        return fileNameList


if __name__ == "__main__":
    filePath = r"E:\workspace\测试文档\集盒大学测试数据\昵称.txt"
    readFile = ReadFile()
    # re = readFile.readFile(filePath)
    # print(len(re))
    # for r in range(0, 10):
    #     print(re[r])

    fileDir = "E:\workspace\测试文档\集盒大学测试数据\课程评论"
    re = readFile.getFileName(fileDir)

    for res in re:
        filePath = res
        fileName = os.path.basename(filePath).split(".")[0]
        print(fileName)
        re = readFile.readFile(filePath)
        print(len(re))
