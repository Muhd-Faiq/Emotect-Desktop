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
    
def returnDecoded():
    return decoded

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
            return response
    else:
        return response
    
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
    print("user_id")
    print(decoded["user_id"])
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


def getUser():  #get _defaultHeaders
    api_url = base_url+"/users"
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    response = requests.get(api_url,headers=headers)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("getusersuccess")
            json_data = json.loads(response.text)
            global users_json_data
            users_json_data=json_data
            return response
            # return response.json()
        except ValueError:
            print("nonoGetUser")



def registerAccount(email,password,name):
    api_url = base_url+"/auths/signup"
    todo = {
        "email": email,
        "password": password,
        "displayName": name
    }
    response = requests.post(api_url, json=todo)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("registersuccess")
            json_data = json.loads(response.text)
            global tempToken
            tempToken=json_data["idToken"]
            getDecoded()
            print(decoded["user_id"])
            createUserProfile(email,name,decoded["user_id"])
            return response
            # return response.json()
        except ValueError:
            return response
    else:
        return response

def createUserProfile(email,name,regid):
    api_url = base_url+"/users/"+regid
    print(tempToken)
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    todo = {
        "email": email,
        "name": name,
        "role": "user"
    }
    response = requests.post(api_url, json=todo,headers=headers)
    print("createUserProfile")
    print(response.status_code)
    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("createUserProfilesuccess")
            return response
            # return response.json()
        except ValueError:
            return response
    else:
        return response
       

def updateDataUser(email,name,dataid):
    api_url = base_url+"/users/"+dataid
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    todo = {
        "email": email,
        "name": name,
        "role": "user"
    }
    response = requests.put(api_url, json=todo,headers=headers)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("updateUserdatasuccess")
            json_data = json.loads(response.text)
            getDecoded()
            return response
            # return response.json()
        except ValueError:
            return response
    else:
        return response



def getDetection():  #get _defaultHeaders
    api_url = base_url+"/emotions"
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    response = requests.get(api_url,headers=headers)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("getemotiondatasuccess")
            json_data = json.loads(response.text)
            global tempArrayJson
            tempArrayJson=[]
            for value_user in users_json_data:
                for value in json_data:
                    if value["userid"]==value_user["id"]:
                        x = { "name": value_user["name"],"email": value_user["email"],"id": value_user["id"]}
                        tempArrayJson.append(x)
                        break
            return response
            # return response.json()
        except ValueError:
            print("nonoGetUser")

def getTempArrayJson():
    return tempArrayJson


def getSpecificDecision(tempuserid):  #get _defaultHeaders
    api_url = base_url+"/emotions?userid="+tempuserid
    bearerToken='Bearer '+tempToken
    headers = {'Content-type': 'application/json', 'Authorization': bearerToken}
    response = requests.get(api_url,headers=headers)

    if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
        try:
            print("getspecificemotionsuccess")
            json_data = json.loads(response.text)
            global users_json_data
            users_json_data=json_data
            return response
            # return response.json()
        except ValueError:
            print("nonoGetUser")