import json
import random
import string

import requests


def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


number = ""
url = "https://cn-geo1.uber.com/signup/clients/validate"

email = ""
deviceImei = random_generator(15, string.digits)
androidId = random_generator(15)
device_serial_number = random_generator(16).upper()
device_id = random_generator(32).lower()
authId = "2309053b68152496a" + random_generator(7, string.digits)
permId = random_generator(32)
deviceLongitude = "12.8396258"
deviceLatitude = "77.6463188"
r_data = {}


def create_account():
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
            "deviceLongitude": deviceLongitude,
            "deviceLatitude": deviceLatitude,
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
        "longitude": deviceLatitude,
        "latitude": deviceLongitude,
        "language": "en_IN",
        "mobile": mob
    }
    headers = {
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'User-Agent': 'client/android/3.115.1',
        'X-Uber-Origin': 'android-client',
        'X-Uber-Device-Location-Latitude': deviceLatitude,
        'X-Uber-Device-Location-Longitude': deviceLongitude,
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

    return jdata


def request_otp(r_data):
    url = "https://cn-geo1.uber.com/rt/users/v2/request-mobile-confirmation"
    header = {
        'x-uber-client-id': 'com.ubercab',
        'x-uber-client-name': 'client',
        'x-uber-client-version': '3.115.1',
        'x-uber-device': 'android',
        'x-uber-device-epoch': '1489424216984',
        'x-uber-device-id': device_id,
        'x-uber-device-ids': 'authId:5360035b08107486a5165920,permId:ce23d81b510e243ea9264f18425bdba5,deviceImei:',
        'x-uber-device-language': 'en_IN',
        'x-uber-device-location-accuracy': '3.948',
        'x-uber-device-location-altitude': '11.495413780212402',
        'x-uber-device-location-course': '0.0',
        'x-uber-device-location-latitude': deviceLongitude,
        'x-uber-device-location-longitude': deviceLatitude,
        'x-uber-device-location-speed': '0.0',
        'x-uber-device-model': 'HM 1S',
        'x-uber-device-mobile': "",
        'x-uber-device-mobile-iso2': 'ca',
        'x-uber-device-os': '4.4.4',
        'x-uber-device-serial': device_serial_number,
        'x-uber-token': r_data["token"],
        'x-uber-protocol-version': '0.73.0',
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'x-uber-client-session': '2c44d768-3a0c-40e0-af8b-ee1d89445886',
        'x-uber-pin-location-latitude': deviceLatitude,
        'x-uber-pin-location-longitude': deviceLongitude,
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '54',
        'Host': 'cn-geo1.uber.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/12.7.2'
    }

    data = {"countryIso2": "ca", "strategy": "default_verification"}
    r = requests.post(verify=False, url=url, data=json.dumps(data), headers=header)
    print(r.text)


def request_call(r_data):
    url = "https://cn-geo1.uber.com/rt/users/request-mobile-confirmation"
    header1 = {
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'User-Agent': 'client/android/3.115.1',
        'X-Uber-Origin': 'android-client',
        'X-Uber-Token': r_data["token"],
        'X-Uber-Id': r_data["uuid"],
        'X-Uber-Device-Location-Latitude': str(deviceLongitude),
        'X-Uber-Device-Location-Longitude': str(deviceLongitude),
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'cn-geo1.uber.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    data = {"country_iso2": "IN", "locale": "en", "strategy": "voice_verification", "user_uuid": r_data["uuid"]}
    r = requests.post(verify=False, url=url, data=json.dumps(data), headers=header1)
    print(r.text)


def add_coupon(r_data):
    coupon = input("Enter Coupon")
    url4 = "https://cn-geo1.uber.com/rt/users/apply-clients-promotions"
    data4 = {"code": coupon, "mnc": "44", "mcc": "404", "confirmed": False}
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
        'x-uber-device-location-latitude': deviceLatitude,
        'x-uber-device-location-longitude': deviceLongitude,
        'x-uber-device-location-speed': '0.0',
        'x-uber-device-model': 'HM 1S',
        'x-uber-device-mobile': '',
        'x-uber-device-mobile-iso2': 'in',
        'x-uber-device-os': '4.4.4',
        'x-uber-device-serial': device_serial_number,
        'x-uber-token': r_data["token"],
        'x-uber-protocol-version': '0.73.0',
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'x-uber-client-session': '2c44d768-3a0c-40e0-af8b-ee1d89445886',
        'x-uber-pin-location-latitude': deviceLatitude,
        'x-uber-pin-location-longitude': deviceLongitude,
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '56',
        'Host': 'cn-geo1.uber.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/12.7.2'
    }
    r4 = requests.post(verify=False, url=url4, data=json.dumps(data4), headers=header3)
    print(r4.text)


def confirm_mobile(r_data):
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
        'x-uber-device-location-latitude': deviceLatitude,
        'x-uber-device-location-longitude': deviceLongitude,
        'x-uber-device-location-speed': '0.0',
        'x-uber-device-model': 'HM 1S',
        'x-uber-device-mobile': '',
        'x-uber-device-mobile-iso2': 'in',
        'x-uber-device-os': '4.4.4',
        'x-uber-device-serial': device_serial_number,
        'x-uber-token': r_data["token"],
        'x-uber-protocol-version': '0.73.0',
        'X-Uber-RedirectCount': '0',
        'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
        'x-uber-client-session': '2c44d768-3a0c-40e0-af8b-ee1d89445886',
        'x-uber-pin-location-latitude': deviceLatitude,
        'x-uber-pin-location-longitude': deviceLongitude,
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


def change_mobile(r_data, e):
    mobile = input("Mobile no ")
    url3 = "https://cn-geo1.uber.com/rt/riders/" + r_data["uuid"]
    header = {'X-Uber-RedirectCount': '0',
              'X-Uber-DCURL': 'https://cn-geo1.uber.com/',
              'User-Agent': 'client/android/3.115.1',
              'X-Uber-Origin': 'android-client',
              'X-Uber-Token': r_data["token"],
              'X-Uber-Id': r_data["uuid"],
              'X-Uber-Device-Location-Latitude': deviceLatitude,
              'X-Uber-Device-Location-Longitude': deviceLongitude,
              'Content-Type': 'application/json; charset=UTF-8',
              'Host': 'cn-geo1.uber.com',
              'Connection': 'Keep-Alive',
              'Accept-Encoding': 'gzip',
              }

    data = {"email": email, "firstName": "Anurag", "lastName": "Singh", "mobile": mobile,
            "mobileCountryIso2": "IN", "hasPassword": False}

    r = requests.patch(verify=False, url=url3, data=json.dumps(data), headers=header)
    print(r.text)


st = "sghdjdgdh"
number = str(input("Mobile No "))
email = input("Email_id ")
mob = "(" + number[:3] + ") " + number[3:6] + "-" + number[6:]
print(mob)
r_data = create_account()
while (st != "exit"):

    print("\n\t*****UberAuto*******\n")
    print("  1. Create_Account")
    print("  2. Request_Otp")
    print("  3. Request_Call")
    print("  4. Confirm_Mobile")
    print("  5. Change_Mobile")
    print("  6. add_coupon")
    st = input()
    if (int(st) == 1):
        number = str(input("Mobile No "))
        email = input("Email_id ")
        mob = "(" + number[:3] + ") " + number[3:6] + "-" + number[6:]
        print(mob)
        r_data = create_account()

    if int(st) == 2:
        request_otp(r_data)
    if int(st) == 3:
        request_call(r_data)
    if int(st) == 4:
        confirm_mobile(r_data)
    if int(st) == 5:
        change_mobile(r_data, email)
    if (int(st) == 6):
        add_coupon(r_data)
