import requests
r=requests.get('https://item.jd.com/3521615.html')
print(r.status_code,r.encoding)
print(r.text[:1000])
print(r.request.headers)