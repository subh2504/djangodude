import json
import random
import string

import requests


def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def create_account(number):
    url = "https://cn-geo1.uber.com/signup/clients/validate"
    mob = "(" + number[:3] + ") " + number[3:6] + "-" + number[6:]
    print(mob)
    email = "subhtest0307201701@gmail.com"
    deviceImei = random_generator(15, string.digits)
    androidId = random_generator(15)
    device_serial_number = random_generator(16).upper()
    device_id = random_generator(32).lower()
    authId = "2309053b68152496a" + random_generator(7, string.digits)
    permId = random_generator(32)
    data = {
        "deviceData": {
            "androidId": androidId,
            "version": "3.115.1",
            "batteryStatus": "discharging",
            "carrier": "Idea",
            "carrierMcc": "404",
            "carrierMnc": "44",
            "sourceApp": "client",
            "cpuAbi": "armeabi, armeabi-v7a",
            "simSerial": random_generator(20, string.digits),
            "deviceIds": {
                "authId": authId,
                "permId": permId,
                "deviceImei": deviceImei
            },
            "phoneNumber": "",
            "md5": "",
            "deviceModel": "HM 1S",
            "deviceOsName": "Android",
            "deviceOsVersion": "4.4.4",
            "ipAddress": "192.168.0.0",
            "imsi": deviceImei,
            "horizontalAccuracy": 10.0,
            "batteryLevel": 0.4,
            "deviceAltitude": 0.0,
            "deviceLongitude": 77.6463188,
            "deviceLatitude": 12.8396258,
            "mockGpsOn": False,
            "rooted": False,
            "locationServiceEnabled": True,
            "course": 200.0,
            "speed": 0.0,
            "unknownSources": True,
            "emulator": False,
            "wifiConnected": True
        },
        "device_ids": {
            "device_imei": deviceImei,
            "googleAdvertisingId": "7e4caf82-8b9a-4482-b8b3-e0eca56d0da8"
        },
        "app": "client",
        "device_serial_number": device_serial_number,
        "mobile_country_iso2": "CA",
        "speed": 0.0,
        "altitude": 0.0,
        "epoch": 1488821661858,
        "device_id": device_id,
        "horizontal_accuracy": 10.0,
        "device_mobile_country_iso2": "in",
        "password": "subh1234",
        "version": "3.115.1",
        "course": 200.0,
        "device_os": "4.4.4",
        "device_model": "HM 1S",
        "device_mobile_digits": "",
        "email": email,
        "device": "android",
        "signup_session_id": "2ec1b1b0-f61f-45c5-ae6b-" + random_generator(10),
        "longitude": 77.6463188,
        "latitude": 12.8396258,
        "language": "en_IN",
        "mobile": mob
    }
    headers = {
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'User-Agent': 'client/android/3.115.1',
        'X-Uber-Origin': 'android-client',
        'X-Uber-Device-Location-Latitude': '12.8396258',
        'X-Uber-Device-Location-Longitude': '77.6463188',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '1467',
        'Host': 'cn-geo1.uber.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }

    r = requests.post(verify=False, url=url, data=json.dumps(data), headers=headers)
    print(r.text)

    data["first_name"] = "Anurag"
    data["last_name"] = "Singh"
    data["token_type"] = "cash"
    data["promotion_code"] = ""

    url1 = "https://cn-geo1.uber.com/signup/clients/create"
    r = requests.post(verify=False, url=url1, data=json.dumps(data), headers=headers)
    print(r.text)

    jdata = json.loads(r.text)
    otp = input("Otp")
    url3 = "https://cn-geo1.uber.com/rt/users/confirm-mobile"

    header3 = {
        'x-uber-client-id': 'com.ubercab',
        'x-uber-client-name': 'client',
        'x-uber-client-version': '3.115.1',
        'x-uber-device': 'android',
        'x-uber-device-epoch': '1488821817817',
        'x-uber-device-id': device_id,
        'x-uber-device-ids': 'authId:' + authId + ',permId:' + permId + ',deviceImei:' + deviceImei,
        'x-uber-device-language': 'en_IN',
        'x-uber-device-location-accuracy': '10.0',
        'x-uber-device-location-altitude': '0.0',
        'x-uber-device-location-course': '0.0',
        'x-uber-device-location-latitude': '12.8396266',
        'x-uber-device-location-longitude': '77.6463191',
        'x-uber-device-location-speed': '0.0',
        'x-uber-device-model': 'HM 1S',
        'x-uber-device-mobile': '',
        'x-uber-device-mobile-iso2': 'in',
        'x-uber-device-os': '4.4.4',
        'x-uber-device-serial': device_serial_number,
        'x-uber-token': jdata["token"],
        'x-uber-protocol-version': '0.73.0',
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'x-uber-client-session': '2c44d768-3a0c-40e0-af8b-ee1d89445889',
        'x-uber-pin-location-latitude': '12.839626',
        'x-uber-pin-location-longitude': '77.646319',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '56',
        'Host': 'cn-geo1.uber.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/12.7.2'
    }

    data3 = {"mobileToken": otp, "strategy": "default_verification"}

    r3 = requests.post(verify=False, url=url3, data=json.dumps(data3), headers=header3)
    print(r3.text)
    url4 = "https://cn-geo1.uber.com/rt/users/apply-clients-promotions"
    data4 = {"code": "apollo2016", "mnc": "44", "mcc": "404", "confirmed": True}
    r4 = requests.post(verify=False, url=url4, data=json.dumps(data4), headers=header3)
    print(r4.text)


number = str(input("Mobile No"))
create_account(number)
