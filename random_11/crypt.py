import base64
import binascii
import hashlib
import json
import secrets

from Crypto.Cipher import AES


class AESCipher:
    def __init__(self, key, iv):
        self.bs = 16
        self.key = key.encode()
        self.iv = iv.encode()

    def encrypt(self, raw):
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(enc))


def enc64(str1, l):
    a = str1.encode()
    md = hashlib.sha256(str1.encode("UTF-8"))
    return binascii.hexlify(md.digest()).decode('ascii')[:l]


def getIV():
    iv = secrets.token_hex(8)
    return iv


key = enc64("Xo0p+AoLQNAgJC7AOwBkFQ4jDWub+Aeaq14c8QvGBw3jiBkdaz1KDg==", 32)
iv = 'a4a3605eb5c08676'
data = "eHwXG9cbmERsjegjkx+OosmazS0LmcI9OIh+yTY6OxV7YlvgFrwbFTm1xGuq+nPmS0fKSA6u21dPjrOj2rS3+pEGHmJRjnymR1g2Qa1+7mDb9Kob9JRKev21b88RAmiKiF66+mkyDIQsrPCUcPE3aIZEXvUjJ/pTbc2uzbQtCmQHrWUEivgOwI86QjaN7WIFUZWqBBzntXlbdA3Z+lFqqL/gIoWp5J1BcoEKybTbXr6F6fKcGtHh2lqBDxJRv30mPjpevY0nafVYi6WgdfTCzZrxwbm8EWbykMtWMGs5LHgzCrbTmNRr7CSZbN27MXRxBYv3nHvGleomRAvUxjgosxH4NxqufyvxTDgvxbMrBYsF30IhBm1dfxdOf7bgA4iaFmWo5ezRWvTpxrab9rs7RG5rBtcDXaufokH/+Ed5xhASAaX44y1VZzXxqn9D82m6g8Cr0VmQTROlifuwbQNm2UlhyMZtf5sixlQWU0kwECAA8V9LNdw3+OzWN+XNmHSHYzJ+xUDiyP6L8eoirC9k6yiUweSIqtdsXPl/KmDh1D6ZzlPhzFyXZTQWx13VOTz4PxTn5WKtaI+SsPCZVoD+D8k5IcUQPNrZdqhChVOZZAkyqgJXVz3/ByY1GeMocs7h"
data1 = {"model": "HM 1S",
         "appmode": "AND",
         "manufacture": "Xiaomi",
         "email": "nilayrai250401@gmail.com",
         "userid": "847767",
         "appversion": "3.0.0",
         "language": "en",
         "handsettype": "xhdpi",
         "advid": "3e86a4ea-aaa3-450e-8aa5-bd0fb5853595",
         "osversion": "4.4.4",
         "celebid": "0",
         "deviceid": "179253570687532"}
a = AESCipher(key, iv)
# phrase = {"data": "none"}
cryp = AESCipher(key, iv)
eTxt = cryp.encrypt(str(json.dumps(data1)))
dTxt = cryp.decrypt(data)
print(str(dTxt))
print(json.loads(dTxt))
