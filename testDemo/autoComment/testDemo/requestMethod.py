import requests
import urllib


class RequestMethod():

    def getData(self,url):
        data = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        return data

    def requestsMethod(self,method,url,data):
        if method == "get":
            response = requests.get(url=url,params=data)
        elif method == "post":
            response = requests.post(url=url, data=data)
        else:
            print("参数错误!!!") 
        return response 



if __name__ == "__main__":
    rs = RequestMethod()
    data = rs.getData("http://www.baidu.com?user=zhu&age=20")
    print(data)



