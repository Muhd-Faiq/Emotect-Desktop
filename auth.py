from lib2to3.pgen2 import token
import requests
import json
import jwt

base_url = "https://us-central1-emotect-bd3d5.cloudfunctions.net/api"
# tempToken=None


def getDecoded():
    global decoded,iduser
    iduser='temp'
    key='super-secret'
    # payload={"id":"1","email":"myemail@gmail.com" }
    # token = jwt.encode(payload, key)
    # print (token)
    decoded = jwt.decode(tempToken, options={"verify_signature": False}) # works in PyJWT >= v2.0
    iduser=decoded["user_id"]
    
    

def signin(email,password):
    api_url = base_url+"/auths/signin"
    todo = {
        "email": email,
        "password": password
    }
    response = requests.post(api_url, json=todo)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("siginsuccess")
            json_data = json.loads(response.text)
            global tempToken
            tempToken=json_data["idToken"]
            getDecoded()
            return response
            # return response.json()
        except ValueError:
            print("nono")
    
    def getToken():
        return tempToken


def postEmotion(emotion,starttime,endtime,date):  #get _defaultHeaders
    api_url = base_url+"/emotions"
    todo = {
        "emotion": emotion,
        "starttime": starttime,
        "endtime": endtime,
        "date": date,
        "userid": decoded["user_id"]
    }
    # print(tempToken)
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    response = requests.post(api_url, json=todo,headers=headers)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("postemotionsuccess")
            json_data = json.loads(response.text)
            return response
            # return response.json()
        except ValueError:
            print("nonoPostEmo")


def getEmotion():  #get _defaultHeaders
    api_url = base_url+"/emotions?userid="+decoded["user_id"]
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    response = requests.get(api_url,headers=headers)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("getemotionsuccess")
            json_data = json.loads(response.text)
            return response
            # return response.json()
        except ValueError:
            print("nonoPostEmo")

       
        