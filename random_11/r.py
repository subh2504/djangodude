import hashlib


# c27ab93c2dfd5cd75b153504f765fd22f74e3ce3065a4e6f284dc0885b5d6b1a907c6c2e5e5afdbb71dc1bc88bbce84ca1554be2a9cd5adfcbe2295351c00cfd
def enc(str1):
    md = hashlib.sha1()
    print(str1.encode())
    md.update(str1.encode())
    return str(md.hexdigest())


d = {
    "isPG": 0,
    "pgAmount": 0,
    "plansSelectionMethod": "manually_entered",
    "rechargeType": "single",
    "walletAmount": 0,
    "ssoToken": "dsfkgbdifsidsffisfdsfds",
    "gcCode": "RCJUO1P3D4EV2BT",
    "orderItems": [{
        "itemPayableAmount": 20,
        "isSpecialRecharge": 0,
        "rechargeTo": "9886648339",
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

data = str(d["totalAmount"]) + "|" + str(d["pgAmount"]) + "|" + str(d["gcCode"]) + "|" + str(d["gcAmount"]) + "|" + str(
    d["gcType"]) + "|" + str(d["walletAmount"]) + "|" + "bGTnLPCUF3e7h2"
data2 = "20.0|0.0|RCJUO1P3D4EV2BT|20.0|WEBPROMOTION|0.0|bGTnLPCUF3e7h2"
print(data)
hexArray = list("0123456789ABCDEF")


def rshift(val, n): return (val % 0x100000000) >> n


def bytesToHex(bArr):
    x = list("\0" * (len(bArr) * 2))

    for i in range(len(bArr)):
        i2 = bArr[i] & 255
        x[i * 2] = hexArray[i2 >> 4]
        x[(i * 2) + 1] = hexArray[i2 & 15]
    # print("__________________"+str(x))
    return "".join(x)


def sha512(data):
    # a = hashlib.sha512(data.encode('utf-8')).digest()
    b = hashlib.sha512(data.encode('utf-8')).hexdigest()
    print()
    return b.lower()


print(sha512(data2))
