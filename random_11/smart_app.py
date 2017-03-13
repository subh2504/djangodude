import hashlib
import json
import time

import requests


def sha512(data):
    # a = hashlib.sha512(data.encode('utf-8')).digest()
    b = hashlib.sha512(data.encode('utf-8')).hexdigest()
    print()
    return b.lower()


def recharge(mobile, coupon):
    v = {
        "isPG": 0,
        "pgAmount": 0,
        "plansSelectionMethod": "manually_entered",
        "rechargeType": "single",
        "walletAmount": 0,
        "ssoToken": "dsfkgbdifsidsffisfdsfds",
        "gcCode": coupon,
        "orderItems": [{
            "itemPayableAmount": 20,
            "isSpecialRecharge": 0,
            "rechargeTo": str(mobile),
            "categoryId": 4,
            "itemAmount": 20,
            "itemDiscount": 0,
            "qty": 1,
            "sTypeId": 2,
            "spId": 2,
            "planId": 0,
            "seqId": 0,
            "cirId": 11
        }
        ],
        "gcAmount": 20,
        "isWallet": 0,
        "gcType": "WEBPROMOTION",
        "totalAmount": 20,
        "savingsPercentage": "0.0",
        "isRecommended": "false",
        "csHash": "d9c2d1ca25b4d2f46035ef9378d4d0cf89abff825c5e0c88e05453735c37243b07e39ee266b2b83c18162b5e784824248e4e562f0aa08b9e7414994f92569548",
        "isGC": 1,
        "chCode": "APP_ANDROID",
        "isPartOfComboRecommendation": "false",
        "user": {
            "phNo": "917089230508",
            "email": "sonika2504@gmail.com",
            "ssoId": "e388f7hbqyspfjhkw8msfj7qm",
            "fName": "Sonika"
        },
        "isOnboarding": "false",
        "deviceId": "49f9868284fc8292",
        "savingsAmount": "0.0"
    }

    a = {
        "isPG": 0,
        "pgAmount": 0,
        "plansSelectionMethod": "manually_entered",
        "rechargeType": "single",
        "walletAmount": 0,
        "ssoToken": "dsfkgbdifsidsffisfdsfds",
        "gcCode": coupon,
        "orderItems": [{
            "itemPayableAmount": 20,
            "isSpecialRecharge": 0,
            "rechargeTo": mobile,
            "categoryId": 4,
            "itemAmount": 20,
            "itemDiscount": 0,
            "qty": 1,
            "sTypeId": 1,
            "spId": 1,
            "planId": 2271,
            "seqId": 0,
            "cirId": 11
        }
        ],
        "gcAmount": 20,
        "isWallet": 0,
        "gcType": "WEBPROMOTION",
        "totalAmount": 20,
        "savingsPercentage": "0.0",
        "isRecommended": "false",
        "csHash": "4804d0c1daf9baab5ea64b409c3c2dea5a4dfb9586553cd5b8ea97a4dcd81fd799919932b707461b44c790adc74c0d8d0501c5fe64ff4e5c2486304cc6f45b8f",
        "isGC": 1,
        "chCode": "APP_ANDROID",
        "isPartOfComboRecommendation": "false",
        "user": {
            "phNo": "917089230508",
            "email": "sonika2504@gmail.com",
            "ssoId": "e388f7hbqyspfjhkw8msfj7qm",
            "fName": "Sonika"
        },
        "isOnboarding": "false",
        "deviceId": "49f9868284fc8292",
        "savingsAmount": "0.0"
    }
    d = a

    hash_key = str(float(d["totalAmount"])) + "|" + str(float(d["pgAmount"])) + "|" + str(d["gcCode"]) + "|" + str(
        float(d["gcAmount"])) + "|" + str(d["gcType"]) + "|" + str(float(d["walletAmount"])) + "|" + "bGTnLPCUF3e7h2"
    print(hash_key)

    csHash = sha512(hash_key)
    print(csHash)
    d["csHash"] = str(csHash)

    url = "https://getsmartapp.com/recharger-api-1.4/recharge/quickRecharge"

    headers = {'App version': '3.2.1',
               'User-Agent': 'Recharge-App',
               'version': '1.4.1',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Content-Length': '1279',
               'Host': 'getsmartapp.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip'
               }
    payload = {"order": json.dumps(d)}

    r = requests.post(verify=False, url=url, data=payload, headers=headers)
    print(r.text)


def addVoucher(coupon):
    millis = int(round(time.time() * 1000))
    d1 = {
        "emailId": "sonika2504@gmail.com",
        "ssoId": "e388f7hbqyspfjhkw8msfj7qm",
        "deviceId": "b583139d1ab67a4",
        "ipAddress": "10.0.2.15",
        "timestamp": str(millis),
        "gcId": coupon
    }

    d1 = {"emailId": "skhdroid@gmail.com",
          "ssoId": "crik0nzhjowt77uu3rf8kak09",
          "deviceId": "aafd2ffebb8fa15a",
          "ipAddress": "10.0.2.16",
          "timestamp": "1489421133034",
          "gcId": coupon
          }

    d1 = {
        "emailId": "santasecret2504@gmail.com",
        "ssoId": "auksga8p534mcnzj3ip47denr",
        "deviceId": "7ccc2474dbedec81",
        "ipAddress": "10.0.2.15",
        "timestamp": str(millis),
        "gcId": coupon
    }

    d = {
        "emailId": "subhashhardaha@gmail.com",
        "ssoId": "83fn6j46j2ddk0w0ehi5pd5v8",
        "deviceId": "39073ea55a80b1b9",
        "ipAddress": "10.0.2.155",
        "timestamp": "1489082296152",
        "gcId": coupon
    }

    data = d["ssoId"] + "|" + d["emailId"] + "|" + "7415842094|" + "-1.0|" + d["timestamp"]
    print(data)

    th = sha512(data)
    print(th)
    url = "https://getsmartapp.com/recharger-api-1.4/wallet/loadGCVoucher"
    headers = {'App version': '3.2.1',
               'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/7.1.19)',
               'version': '1.4.1',
               'Content-Type': 'application/json',
               'Host': 'getsmartapp.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'transactionHash': th,
               }
    r = requests.post(verify=False, url=url, data=json.dumps(d), headers=headers)
    print(r.text)


# recharge("7415842094","RCJEMROVEEG7DGG")
a = "xxxx"
while (a != "stop"):
    a = input().strip()
    addVoucher(str(a))
