import requests
import tokenGeneratorService as selfGenTokenSvc
import firebaseAuthService as fieryTokenSVC

def getTokenFromTokenGeneratorService():
    userEmail = "test.user@email.com"
    userName = "testuser"
    token = selfGenTokenSvc.generateToken(userEmail, userName)
    return token

def getTokenFromFirebaseAuthService():
    userEmail = "test.user@email.com"
    password = "123456"
    token = fieryTokenSVC.getToken(userEmail, password)
    return token

def loginWithSelfGeneratedToken():
    token = getTokenFromTokenGeneratorService()

    headers = {"jwtTokenString": token, 
               "Content-Type": "application/json"}
    # headers = {"Content-Type": "application/json"}

    url = "https://us-east-2.aws.data.mongodb-api.com/app/nswcstest-dixnp/endpoint/nswcs_endpoint"
    data = {"foo": "bar"}

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

def loginWithFirebaseToken():
    token = getTokenFromFirebaseAuthService()
    print(token)

    headers = {"jwtTokenString": token, 
               "Content-Type": "application/json"}
    # headers = {"Content-Type": "application/json"}

    url = "https://us-east-2.aws.data.mongodb-api.com/app/nswcstest-dixnp/endpoint/nswcs_endpoint"
    data = {"foo": "bar"}

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

if __name__ == "__main__":
    # loginWithSelfGeneratedToken()
    loginWithFirebaseToken()







