import requests
kv = {'key1': 'value1', 'key2': 'value2'}
print(kv)
r = requests.request(method='GET',url='http://python123.io/ws', params = kv)
print(r.url)
r = requests.request('POST','http://python123.io/ws',data=kv)
print(r.url)
hd={'user-agent':'Chrome/10'}
r=requests.request('POST','http://python123.io/ws',headers=hd)
print(r.headers)
pxs={'http':'http://user:pass@10.10.1:1234'
    'http':'http://10.10.1:4321'}
r = requests.request('GET',''http://python123.io/ws',proxies=pxs)