import requests
kv={'User-Agent':'Mozilla/5.0'}#改变头部信息
r=requests.get('https://www.amazon.cn/s/ref=sa_menu_ags_l3_huwaibeibao?_encoding=UTF8&rh=n%3A1403206071%2Cn%3A836312051%2Cn%3A%21836313051%2Cn%3A1488665071&srs=1403206071',headers=kv)
print(r.status_code,r.encoding)
r.encoding=r.apparent_encoding
print(r.text[:1000])
print(r.request.headers)