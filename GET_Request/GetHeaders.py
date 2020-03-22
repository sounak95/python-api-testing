import requests

header_data={"T1":"First Header","T2":"Second Header"}
url="https://httpbin.org/get"
response=requests.get(url,headers=header_data)
print(response.text)