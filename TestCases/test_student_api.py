import requests
import json
import jsonpath

def test_add_student_data():
    app_url="http://thetestingworldapi.com/api/studentsDetails"
    f=open("D:/ApiTestingProject/TestCases/AddStudentData.json","r")
    json_request= json.loads(f.read())
    response =requests.post(app_url,json_request)
    print(response.text)

def test_get_student_data():
    app_url = "http://thetestingworldapi.com/api/studentsDetails/163201"
    response=requests.get(app_url)
    print(response.text)
    # json_response=json.loads(response.text)
    json_response = response.json()
    print(json_response)
    id=jsonpath.jsonpath(json_response,"data.id")
    print(id)
    assert id[0]==163201

def test_update_student_data():
    app_url="http://thetestingworldapi.com/api/studentsDetails/163201"
    f=open("D:/ApiTestingProject/TestCases/UpdateStudentData.json","r")
    json_request= json.loads(f.read())
    response =requests.put(app_url,json_request)
    print(response.text)
    json_response = response.json()
    # id = jsonpath.jsonpath(json_response, "id")
    # assert id[0] == 163201

def test_delete_student_data():
    app_url = "http://thetestingworldapi.com/api/studentsDetails/163201"
    response=requests.delete(app_url)
    print(response.text)
    # json_response=json.loads(response.text)
