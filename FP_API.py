import requests
import json
from requests.auth import HTTPBasicAuth
import pandas as pd
from pprint import pprint


auth = {
        'username': 'x',
        'password': 'x',
        'token': '',
        'refresh': '',
        'cert': False
        }

# Generates Token

path = "/api/fmc_config/v1/domain"
resp = requests.post(f"https://x.x.x.x/api/fmc_platform/v1/auth/generatetoken",
                      auth=HTTPBasicAuth(auth['username'], auth['password']),
                      data={},
                      verify=auth['cert'])
auth['token'] = resp.headers['X-auth-access-token']
auth['refresh_token'] = resp.headers['X-auth-refresh-token']


path = path + "/" + resp.headers['DOMAIN_UUID']
token_url = "https://x.x.x.x/api/fmc_platform/v1/auth/generatetoken"


my_headers = {
        'Content-Type': 'application/json',
        'X-auth-access-token': auth['token']
        }

# GET Request

resp = requests.get("https://x.x.x.x/api/fmc_config/v1/domain/(DOMAIN_UUID)/health/alerts",
                    headers=my_headers,
                    verify=auth['cert'])
if resp.status_code == 200:
    print("="*50)
    result = resp.json()


df = pd.DataFrame.from_dict(result["items"])
print(df)

# Converting a data frame to csv:
df.to_csv("FP_API")