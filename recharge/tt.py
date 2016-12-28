import requests
import json
import time
# Create your views here.
#100_  288364922865768 0825999060 s67phvi7-dqah-94pd-qna4-ciu5tsbwsr0e

#100 297544743409655 0672084625 b22fpf2i-383s-u853-s26u-d75o77kok2wy

import string
import random


def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

otp = ""
deviceId = random_generator(15, string.digits)
mobile = random_generator(10, string.digits)
advertiserId = str(random_generator(8) + "-" + random_generator(4) + "-" + random_generator(4) + "-" + random_generator(4) + "-" + random_generator(12))
#deviceId="200790378610362"
#mobile="8601186468"
#advertiserId="fzlqqmsn-07aq-faar-6j9e-uk7a8seottzr"
androidId = random_generator(16)
print(deviceId, mobile, advertiserId, otp)


def getWalletInfo():
    url = "http://event.aliveonescan.com/appserver/rest/api/v1/getWalletInfo"
    data = {
        "deviceId": deviceId,
        "mobile": mobile,
        "androidId": androidId,
        "isRooted": False,
        "serviceType": "RECHARGE",
        "appVersion": "4.4.1",
        "advertiserId": advertiserId.upper()
    }
    headers = {'content-type': 'application/json',
               'connection': 'Keep-Alive',
               'host': 'event.aliveonescan.com',
               'Content-Language': 'en-US',
               'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/6.8.25)',
               'accept-encoding': 'gzip',
               }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(r.text)
    print(json_data)
    print(json_data["data"]["walletAmount"])
    return json_data["data"]


def otpgen(deviceId, mobile):
    url = "http://event.aliveonescan.com/ServiceIntegration/otpgen"
    data = {
        "deviceId": deviceId,
        "mobile": mobile
    }
    headers = {'content-type': 'application/json',
               'connection': 'Keep-Alive',
               'host': 'event.aliveonescan.com',
               'Content-Language': 'en-US',
               'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/6.8.25)',
               'accept-encoding': 'gzip',
               }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(r.text)
    print(json_data)
    otp = json_data["Results"][0]["otp"]
    # if json_data['status'] == "OK":
    #   print(")(")

    url = "http://event.aliveonescan.com/ServiceIntegration/verifyotp"
    data = {
        "deviceId": deviceId,
        "mobile": mobile,
        "otp": otp
    }
    print("**********")
    print(data)
    headers = {'content-type': 'application/json',
               'connection': 'Keep-Alive',
               'host': 'event.aliveonescan.com',
               'Content-Language': 'en-US',
               'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/6.8.25)',
               'accept-encoding': 'gzip',
               }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(r.text)
    print(json_data)


def campaytm():
    url = "http://www.alivear.com/aliveservices/api/campaytm"

    data = {"markerid": "0",
            "model": "HM 1S",
            "countrycode": "",
            "location": "null-null-",
            "servicename": "alivelite",
            "appuser": "0", "serviceid": "5001", "city": "",
            "deviceid": deviceId,
            "ip": str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
                random.randint(0, 255)) + "." + str(random.randint(0, 255)),
            "version": "4.4.1",
            "mode": "AND",
            "pincode": "",
            "dealer": "0", "locradius": "50",
            "manufacture": random_generator(9),
            "longitude": 54.6463191,
            "language": "en",
            "locunit": "Kms",
            "latitude": 32.8396266}

    headers = {'content-type': 'application/json',
               'connection': 'Keep-Alive',
               'host': 'www.alivear.com',
               'Content-Language': 'en-US',
               'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/6.8.25)',
               'accept-encoding': 'gzip',
               }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(r.text)
    print(json_data)

    rurl=json_data["url"]
    headers = {'content-type': 'application/json',
               'connection': 'Keep-Alive',
               'host': 'event.aliveonescan.com',
               'Content-Language': 'en-US',
               'referer':rurl,
               'user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/6.8.25)',
               'accept-encoding':'deflate,sdch',
               }
    a="st"
    while(a!="stop"):
        a=input()
        print("Applying "+a)
        url="http://event.aliveonescan.com/ServiceIntegration/check_code?code="+a+"&deviceid="+deviceId+"&version=&amount=&deviceIdCheck="
        r = requests.get(url=url,headers=headers)


def recharge():
    json_data=getWalletInfo()
    print("*******   Recharge    *******")
    rMsisdn=input("Enter Mobile")


    opr = input("Enter operator")
    uType=input("Y:Postpaid  N:Prepaid")

    amt = int(input("Enter Amaount"))

    url = "http://event.aliveonescan.com/os/award.docg"

    headers = {'content-type': 'application/json',
               'connection': 'Keep-Alive',
               'host': 'www.alivear.com',
               'Content-Language': 'en-US',
               'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/6.8.25)',
               'accept-encoding': 'gzip',
               }
    data= {"uType": uType.upper(), "rMsisdn": rMsisdn, "price": str(amt), "sType": "M", "operator": opr,
         "uMsisdn": mobile, "deviceid": deviceId}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(r.text)
    print(json_data)


otpgen(deviceId, mobile)

getWalletInfo()
otpgen(deviceId,mobile)
st = ""
while (st != "exit"):

    print("\n\t*****PyCharge*******\n")
    print("  1. Wallet balance")
    print("  2. Profile Details")
    print("  3. Reedem Voucher")
    print("  4. Recharge")
    print("  5. Verify Mobile")
    st = input()
    if (int(st) == 1):
        getWalletInfo()
    if (int(st) == 2):
        print(deviceId, mobile, advertiserId, otp)
    if (int(st) == 3):
        campaytm()
    if (int(st) == 4):
        recharge()
    if (int(st)==5):

        inp=input("Enter profile").split()
        deviceId=inp[0]
        mobile=inp[1]
        advertiserId=inp[2]

        otpgen(deviceId,mobile)



def xyz():
    a = []
    inp = input()
    while (inp != "stop"):
        a.append(inp)
        inp = input()
    print(len(a))
    b = list(set(a))
    print(len(b))
    for i in b:
        print(i)
