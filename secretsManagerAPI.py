import boto3
from botocore.exceptions import ClientError
import requests, json

def get_APIKey():

    secret_name = "nswcs_api_key"
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

    return secret

if __name__ == "__main__":
    secret = json.loads(get_APIKey()).get("nswcs_api_key")
    # NO API KEY
    # headers = {"Content-Type": "application/json"}

    # ONLY API KEY and NO SECRET - no need of secret in app service
    headers = {"apiKey": secret, 
               "Content-Type": "application/json"}

    # CORRECT API KEY but WRONG SECRET
    # headers = {"apiKey": secret, 
    #            "Content-Type": "application/json",
    #            "Secret": secret} 

    # CORRECT API and SECRET
    # headers = {"apiKey": secret, 
    #            "Content-Type": "application/json",
    #            "Secret": "8R3yF4hdd4X6Mj4PJs1SV16qTL7BIhx9DXVdV8R9zBJ4iwucxP2dEixsE8SRGdj8"}



    url = "https://us-east-2.aws.data.mongodb-api.com/app/nswcstest-dixnp/endpoint/nswcs_endpoint"
    data = {"foo": "bar"}

    response = requests.post(url, headers=headers, json=data)
    try:
        print(response.json())
    except Exception as err:
        print(response)



