import requests
import json
import jsonpath
url="https://reqres.in/api/users"
import pytest

a=10

@pytest.fixture
def start_exec():
    global file
    file = open('D:\\ApiTestingProject\\TestCases\\CreateNewResource.json', 'r')

@pytest.mark.smoke
def test_create_new_resource(start_exec):

    json_input=file.read()
    request_json=json.loads(json_input)
    print(request_json)

    #Make post request with json input body

    response = requests.post(url,request_json)
    print(response.content)
    assert response.status_code==201

@pytest.mark.skip("this is not suitable for current build")
def test_create_other_new_resource(start_exec):
    file = open('D:\\ApiTestingProject\\TestCases\\CreateNewResource.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    print(request_json)

    #Make post request with json input body

    response = requests.post(url,request_json)


    print(response.headers)

    print(response.headers.get('Content-Length'))

    # Parse response to json format
    json_response = json.loads(response.text)
    print(json_response)

    id= jsonpath.jsonpath(json_response,'id')
    print(id[0])

@pytest.mark.skipif(a>=10,reason="this is not suitable for current build")
def test_create_other_new_resource1(start_exec):
    file = open('D:\\ApiTestingProject\\TestCases\\CreateNewResource.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    print(request_json)

    #Make post request with json input body

    response = requests.post(url,request_json)


    print(response.headers)

    print(response.headers.get('Content-Length'))

    # Parse response to json format
    json_response = json.loads(response.text)
    print(json_response)

    id= jsonpath.jsonpath(json_response,'id')
    print(id[0])

