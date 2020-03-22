import requests

param={'name':'Sounak','email':'sounak95@gmail.com','number':'9038382826'}
url="https://httpbin.org/get"
response=requests.get(url,params=param)
print(response.text)