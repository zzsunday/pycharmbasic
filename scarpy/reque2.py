import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#如果状态码不是200，则产生异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "error"

if __name__== "__main__":
    url="www.baidu.com"
    print(getHTMLText(url))

#还是得理解下__name__的用法
#异常的用法
