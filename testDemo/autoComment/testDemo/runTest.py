import json
from requestMethod import RequestMethod


class TestDemo():

    def __init__(self,mobile): 
        self.urlAll = "http://test.eweixue.com/v1/user/auth/test_login?mobile=" + mobile

        self.url = "http://test.eweixue.com/v1/user/auth/test_login?"


    
    def test1(self):
        requestTest = RequestMethod()
        data = requestTest.getData(self.urlAll)

        response = requestTest.requestsMethod("post",self.url,data).json()
        print(response)

if __name__ == "__main__":
    test = TestDemo()
    test.test1()