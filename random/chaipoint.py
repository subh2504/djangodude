import json
import requests
from requests.auth import HTTPBasicAuth

money=""
username="7089230508"
pwd="subh1234"
ti=""

token= ""
def login():
    url = "https://api.urbanpiper.com/api/v1/auth/me/?format=json"

    headers = {'X-Device': 'ANDROID',
                'X-App-Version': '3.159.13.93',
                'Host': 'api.urbanpiper.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/2.4.0',
               }
    r = requests.get(url=url, headers=headers,auth=HTTPBasicAuth("+91"+username+"__73574477", pwd),verify=False)
    #json_data = json.loads(r.text)
    print(r.text)

def initPayment():
    amt=int(input("Enter Amount "))*100
    url = "https://api.urbanpiper.com/payments/init/73574477/?channel=app_android&amount="+str(amt)+"&purpose=reload"

    headers = {'X-Device': 'ANDROID',
              'X-App-Version': '3.159.13.93',
              'Host': 'api.urbanpiper.com',
              'Connection': 'Keep-Alive',
              'Accept-Encoding': 'gzip',
              'User-Agent': 'okhttp/2.4.0',
              }
    r = requests.get(url=url, headers=headers, auth=HTTPBasicAuth("+91" + username + "__73574477", pwd), verify=False)
    json_data = json.loads(r.text)
    ti=json_data["transaction_id"]

    url="https://api.urbanpiper.com/payments/callback/"+ti+"?gateway_txn_id=pay_6DtArudG2DIecD&failed=0"
    headers = {'X-Device': 'ANDROID',
               'X-App-Version': '3.159.13.93',
               'Host': 'api.urbanpiper.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/2.4.0',
               }

    r = requests.get(url=url, headers=headers, auth=HTTPBasicAuth("+91" + username + "__73574477", pwd), verify=False)
    print(r.text)


login()
initPayment()