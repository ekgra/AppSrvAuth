import requests
import tokenGeneratorService as tokenSvc

def getJWTtokenFromService():
    userEmail = "kuber.gaur@email.com"
    userName = "Kuber"
    token = tokenSvc.generateToken(userEmail, userName)
    return token

if __name__ == "__main__":
    token = getJWTtokenFromService()

    headers = {"jwtTokenString": token, 
               "Content-Type": "application/json"}
    # headers = {"Content-Type": "application/json"}

    url = "https://us-east-2.aws.data.mongodb-api.com/app/nswcstest-dixnp/endpoint/nswcs_endpoint"
    data = {"foo": "bar"}

    response = requests.post(url, headers=headers, json=data)
    print(response.json())




# curl -H "jwtTokenString: ***"
