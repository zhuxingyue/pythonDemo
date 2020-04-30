import os
import json

class ReadText(object):

    fileNamePath = "/Users/zhuxingyue/Documents/workspace/myworkspace/pythonDemo/testDemo/autoComment/testDemo/name.txt"

    def getUserName(self):
        with open(self.fileNamePath,'r') as fb:
            data = fb.read()
            data = data.split("\n")
            #data.json()
            print(data)
        return data
    

if __name__ == "__main__":
    read = ReadText()
    read.getUserName()


