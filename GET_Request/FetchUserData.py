import requests
import json
import jsonpath
# API Urls

url= "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)
print(response.content)
print(response.headers)

# Validate Status code
print(response.status_code)

assert response.status_code==200

#Fetch specific data from response header
print(response.headers.get("Date"))
print(response.headers.get("Server"))
#Fetch cookies
print(response.cookies)
print(response.encoding)
print(response.elapsed)

# Parse response to json format
json_response = json.loads(response.text)
print(json_response)

#Fetch value using JsonPath
pages= jsonpath.jsonpath(json_response,'total_pages')
assert pages[0]==2

first_name=jsonpath.jsonpath(json_response,'data[2].first_name')
print(first_name[0])

# size=jsonpath.jsonpath(json_response,'data.size')
# print(size)


for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])

