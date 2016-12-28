import json

import requests
from requests.auth import HTTPBasicAuth

def login():
    url = "https://slide-api.42.company/api/v1/entries?sim_operator_name=DEFACE&network_operator_name=DEFACE&connected_network_type=wifi"

    headers = {
        'Accept-Language': 'en-IN',
        'User-Agent': 'Slide/1.2.34 (Dalvik/1.6.0; Android/4.4.4; U; HM 1S; Xiaomi)',
        'X-Slide-API-Revision': '9',
        'X-Slide-Android-App-Version-Code': '104',
        'Authorization': 'Token token="fyBUyzsQXS1o9X8BJfdqVsV3YPp5GuaJHQ"',
        'X-Slide-Signature': 'R0VUJmh0dHBzJTNBJTJGJTJGc2xpZGUtYXBpLjQyLmNvbXBhbnklMkZhcGklMkZ2MSUyRmVudHJpZXMmY29ubmVjdGVkX25ldHdvcmtfdHlwZT13aWZpJm5ldHdvcmtfb3BlcmF0b3JfbmFtZT1ERUZBQ0Umc2ltX29wZXJhdG9yX25hbWU9REVGQUNF',
        'Host': 'slide-api.42.company',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
               }
    r = requests.get(url=url, headers=headers,verify=False)
    json_data = json.loads(r.text)
    id=json_data["entries"]
    x=[]
    s="["
    for i in id:
        print(i["extra"]["impression_reward"])
        x.append(i["id"])
        s=s+str(i["id"])+","

    print(s+"]")

login()