import requests
import json
import jsonpath

def test_end_to_end():
    app_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("D:/ApiTestingProject/TestCases/AddStudentData.json", "r")
    json_request = json.loads(f.read())
    response = requests.post(app_url, json_request)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url="http://thetestingworldapi.com/api/technicalskills"
    f = open("D:/ApiTestingProject/TestCases/TechDetails.json", "r")
    json_request = json.loads(f.read())
    json_request['id']=int(id[0])
    response = requests.post(tech_api_url, json_request)
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/addresses"
    f = open("D:/ApiTestingProject/TestCases/Address.json", "r")
    json_request = json.loads(f.read())
    json_request['stId'] = id[0]
    response = requests.post(add_api_url, json_request)
    print(response.text)

    fnal_details_url="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(fnal_details_url)
    print(response.text)