import requests
import json
import jsonpath
url="https://reqres.in/api/users"

file = open('CreateNewResource.json','r')
json_input=file.read()
request_json=json.loads(json_input)
print(request_json)

#Make post request with json input body

response = requests.post(url,request_json)
print(response.content)
assert response.status_code==201

print(response.headers)

print(response.headers.get('Content-Length'))

# Parse response to json format
json_response = json.loads(response.text)
print(json_response)

id= jsonpath.jsonpath(json_response,'id')
print(id[0])

