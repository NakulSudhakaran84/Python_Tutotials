import requests

res=requests.get("http://www.google.com")
print(res)
print(res.cookies)
print(res.url)
print(res.status_code)
print(res.text)