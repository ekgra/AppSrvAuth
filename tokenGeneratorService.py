import boto3
from botocore.exceptions import ClientError
import json, jwt
from datetime import datetime

def getTokenSecretFromAWS():

    secret_name = "nswcs_jwt_secret"
    region_name = "eu-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return json.loads(secret)

def generateToken(sub, name):
    secret = getTokenSecretFromAWS()
    #print(secret['nswcs_jwt_secret'], secret['nswcs_app_srvc_name'])

    iat = datetime.now().timestamp() - (1 * 60)
    exp = iat + (31 * 60)

    jwtPayload = {
        "sub": sub, # similarly can get the user details from the login context of user in the application
        "name": name,
        "aud": secret['nswcs_app_srvc_name'],
        "exp": exp,
        "iat": iat
    }

    encodedJWT = jwt.encode(payload=jwtPayload, key=secret['nswcs_jwt_secret'], algorithm="HS256")
    #decodedJWT = jwt.decode(jwt=encodedJWT, key=secret['nswcs_jwt_secret'], algorithms="HS256", audience=secret['nswcs_app_srvc_name'])

    return encodedJWT


if __name__ == "__main__":
    token = generateToken("kuber.gaur@email.com", "Kuber")
    print(token)

# jwt signature secret : Vnxd4HE7FS0vpBgl51Mh2JUf6KLuwQ8N
# token = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrdWJlci5nYXVyQGVtYWlsLmNvbSIsIm5hbWUiOiJLdWJlciIsImlhdCI6MTY3NDI5NzAzNiwiZXhwIjoxNzA1ODMzMDM2LCJhdWQiOiJuc3djc3Rlc3QtZGl4bnAifQ.wRHqj-q9q1upCWsw1gwG2cQvh5bXo6gMFtez-Q0lJ7g










# curl -s -H "apiKey: **" -H "Secret: **"
# api - {nswcs_api_key: eUJG9pnlpdqDgVB3VPmGRZoGzFZbqCPkzFBb1qLYpCDXb8MmrYSSmAPxUmT1BeDX}
# secret 8R3yF4hdd4X6Mj4PJs1SV16qTL7BIhx9DXVdV8R9zBJ4iwucxP2dEixsE8SRGdj8