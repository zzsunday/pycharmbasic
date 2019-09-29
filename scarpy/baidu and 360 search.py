import requests
try:
    kv={'wd':'python'}
    r=requests.get('https://www.baidu.com',params=kv)
    print(r.status_code)
    print(r.request.url)
    print(len(r.text))
except:
    print('error')