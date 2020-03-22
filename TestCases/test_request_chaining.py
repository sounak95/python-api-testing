import requests
import json
import jsonpath


def test_add_new_student():
    global id
    app_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("D:/ApiTestingProject/TestCases/AddStudentData.json", "r")
    json_request = json.loads(f.read())
    response = requests.post(app_url, json_request)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_fet_student_details():
    fnal_details_url = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(fnal_details_url)
    print(response.text)