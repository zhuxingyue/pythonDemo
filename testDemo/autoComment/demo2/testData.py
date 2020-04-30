from readFile import ReadFile
from sqlRead import DBconnect
import os
from login import Login
from comment import Comment
import time 
import threading
from updateUser import UpdateUser


class TestDmeo():
    # 评论文件地址
    fileDir = "E:\workspace\测试文档\集盒大学测试数据\课程评论"

    # 获取课程名称,查询课程id
    def getCourseName(self):
        courseInfo = {}

        readFile = ReadFile()
        db = DBconnect()

        fileNamePaths = readFile.getFileName(self.fileDir)

        for fileNamePath in fileNamePaths:
            fileName = os.path.basename(fileNamePath).split(".")[0]

            sql = "select course_id from jh_course where title = '" + fileName + "'"

            dbc = db.dbConn()
            idList = db.search(dbc, sql)
            db.dbClose(dbc)

            courseInfo.setdefault(fileName, idList[0])
        return courseInfo

    # 获取课程对应的评论
    def getCourseComment(self):
        courseCommentInfo = {}
        readFile = ReadFile()

        fileNamePaths = readFile.getFileName(self.fileDir)
        for fileNamePath in fileNamePaths:
            fileName = os.path.basename(fileNamePath).split(".")[0]
            comList = readFile.readFile(fileNamePath)
            courseCommentInfo.setdefault(fileName, comList)
        return courseCommentInfo

    # 获取用户电话号码,生成对应的token
    def getMoblie(self):
        tokenList = []
        sql = "select mobile from jh_customer_login where mobile like '1521234%'"
        db = DBconnect()
        dbc = db.dbConn()
        mobileList = db.search(dbc, sql)
        db.dbClose(dbc)

        for mobile in mobileList:
            login = Login(mobile=mobile)
            token = login.login()
            tokenList.append(token)
        return tokenList

    # 获取用户名称和头像
    def getUserName(self):
        userInfo = {}
        filePath = ""

        readFile = ReadFile()
        nameList = readFile.readFile(filePath)

        db = DBconnect()
        dbc = db.dbConn()
        imageList = db.search(dbc)
        db.dbClose(dbc)

        for i in range(0,len(nameList)):
            userInfo.setdefault(nameList[0],imageList[0])

        return userInfo



if __name__ == "__main__":
    test = TestDmeo()

    courseInfo = test.getCourseName()
    courseNames = courseInfo.keys()
    # print(courseInfo)
    courseCommentInfo = test.getCourseComment()
    # print(courseCommentInfo)
    userInfo = test.getUserName()

    tokenList = test.getMoblie()

    t1 = threading.Thread(target=upUser,args=(tokenList,userInfo))
    t1.start()

    index = 0
    for courseName in courseNames:
        comments = courseCommentInfo.get(courseName)
        for comment in comments:
            com = Comment(course_id=courseInfo.get(courseName), token=tokenList[0])
            com.userComment(message=comment)
            index+=1
            time.sleep(2)

    def upUser(tokenList,userInfo):
        names = userInfo.keys()
        images = userInfo.values()
        for index in range(len(tokenList)):
            up = UpdateUser(tokenList[index])
            up.updateUserName(names[index])
            up.updateUserHeadImage(images[index])



