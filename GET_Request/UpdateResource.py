import requests
import json
import jsonpath
# API Urls

url= "https://reqres.in/api/users/2"

file = open('UpdateResource.json','r')
json_input=file.read()
request_json=json.loads(json_input)
print(request_json)

#Make post request with json input body

response = requests.put(url,request_json)
print(response.content)
assert response.status_code==200

print(response.headers)

print(response.headers.get('Content-Type'))

# Parse response to json format
json_response = json.loads(response.text)
print(json_response)

job= jsonpath.jsonpath(json_response,'job')
print(job[0])