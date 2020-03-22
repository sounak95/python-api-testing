import requests
import json
import jsonpath


def test_basic_auth():
    app_url = "https://api.github.com/user"
    response= requests.get(app_url,auth=requests.auth.HTTPBasicAuth('git_username','git_password'))
    print(response.text)

def test_oAuth():
    token_url="http://thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'admin','password':'abc'}
    response=requests.post(token_url,data)
    print(response.text)
    token_value=jsonpath.jsonpath(response.json(),'access_token')

    auth={'Authorization': 'Bearer ' +token_value[0]}
    url = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(url,headers=auth)
    print(response.text)
