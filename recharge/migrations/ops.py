import requests
import json
import time
# Create your views here.


import string
import random


def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


deviceId = random_generator(15, string.digits)
mobile = random_generator(10, string.digits)
otp = ""
advertiserId = str(random_generator(8) + "-" + random_generator(4) + "-" + random_generator(4) + "-" + random_generator(
    4) + "-" + random_generator(12))
androidId = random_generator(16)
print(deviceId, mobile, advertiserId, otp)


def optts():
    url = "https://account.oneplus.net/login"
    a=input()
    data = {
        '_token': 'Ef6heVMC7Y18s2BwQH6Xpgyhp36stnhkWxi5AOiX',
        'return_to': 'https://oneplusstore.in/december?_act_referrer=10495584',
        'email': a,
        'password': a,
    }

    headers = {
        'Host': 'account.oneplus.net',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Origin': 'https://account.oneplus.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://account.oneplus.net/login?_act_referrer=10495584',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cookie': '__cfduid=deef8b73d3c7ff584ef7475af83f5b5d11481811898; _act_referrer=10495584; opcid=1481811980221_1601064166; oppt=oneplus; _gat_UA-46480385-1=1; _dc_gtm_UA-46480385-29=1; __utmt=1; __sonar=2197051504857589229; km_ai=lusJKC1d7lf0Tt3%2BHw05DVnjLPg%3D; km_uq=; lty=local; _sscid=19655208; lbid=rB8MoVhSqV0ST1/FBI8JAg==; AWSELB=2BBFC14C1989DF2D57D5FDFBF1B669B9C5A726EEE1B84C2CD20FC18C14753B409CE8BBF6A110591021573D10A3A189BB9A9AA2EDBA3441947B92E44C43602E0AF8491909069B97E60DDDE4609F80C7BE819B742C; refererstore=in; return_to=https%3A%2F%2Foneplusstore.in%2Fdecember; laravel_session=eyJpdiI6Im5TaTFQVlh4d0Q3Sm1BSis5aFpDZm9qUFlpUVh1SzJDeERzeG5FaUFHSHc9IiwidmFsdWUiOiJGZ1FLMWZaK3UxWVJcL25cL29sZE5tTnhnU2pNcnpTUUpDUjVIdVpMdWk3ZU13bGJBaWR4c0c3UFpISzcwTW1vM2hKQk5lcm1nYUJ6Q0gya0pXdlZoUWp3PT0iLCJtYWMiOiI4MjNiODEzNDExZjhjZDkwMDRjOTA2ZDRjZDUxMzI3NDExYTRmNjQyZWI3Mzk3YTUxOTU0Mjg4ZjQ2NjNjNzhkIn0%3D; AWSELB=699D5D25125B0EE34BEE1A326290BE978B7FF8A3D9A69645DEC5711DC898D878B157191C104DC7AECC97721C4AC5F24973D98DF216D47B621BCF2072B4A8495F4C39EB196A; cartItemQuantity=0; __utma=111174676.694323396.1481811980.1481811980.1481811980.1; __utmb=111174676.2.10.1481811980; __utmc=111174676; __utmz=111174676.1481811980.1.1.utmcsr=oneplusstore.in|utmccn=(referral)|utmcmd=referral|utmcct=/december; opsid=1481811980221_37473807; opsct=1481811980222; opbct=1481811980222; opnt=1481812322519; opstep=2; optime_browser=1481812322518; opstep_event=0; opnt_event=1481812322519; _ga=GA1.3.694323396.1481811980; _ga=GA1.2.694323396.1481811980; kvcd=1481812323611; km_vs=1; km_lv=1481812324'
    }
    r = requests.post(url, data=data, headers=headers)

    print(r.text)



optts()





