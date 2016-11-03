from django.shortcuts import render, get_object_or_404
from .models import User, AliveVoucher,BMSVoucher
import requests
from django.http import HttpResponse,HttpResponseRedirect
import json
import time
from django.core.urlresolvers import reverse
# Create your views here.


import string
import random


def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


MANUFACTURER = ['Amoi', 'Coolpad', 'Gfive', 'Highscreen', 'MTS', 'teXet', 'Yotaphone', 'Haier', 'Huawei', 'Lenovo',
                'Meizu', 'Oppo', 'QiKU', 'Smartisan', 'Vivo', 'Wasam', 'Zopo', 'ZUK']

NAME = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
        "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
        "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young", "Allen",
        "Sanchez", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez", "Campbell",
        "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins", "Edwards",
        "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers", "Morgan", "Peterson", "Cooper",
        "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox", "Diaz", "Richardson", "Wood", "Watson",
        "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz", "Hughes", "Price", "Myers", "Long", "Foster", "Sanders",
        "Ross", "Morales", "Powell", "Sullivan", "Russell", "Ortiz", "Jenkins", "Gutierrez", "Perry", "Butler",
        "Barnes", "Fisher", "Henderson", "Coleman", "Simmons", "Patterson", "Jordan", "Reynolds", "Hamilton", "Graham",
        "Kim", "Gonzales", "Alexander", "Ramos", "Wallace", "Griffin", "West", "Cole", "Hayes", "Chavez", "Gibson",
        "Bryant", "Ellis", "Stevens", "Murray", "Ford", "Marshall", "Owens", "Mcdonald", "Harrison", "Ruiz", "Kennedy",
        "Wells", "Alvarez", "Woods", "Mendoza", "Castillo", "Olson", "Webb", "Washington", "Tucker", "Freeman", "Burns",
        "Henry", "Vasquez", "Snyder", "Simpson", "Crawford", "Jimenez", "Porter", "Mason", "Shaw", "Gordon", "Wagner",
        "Hunter", "Romero", "Hicks", "Dixon", "Hunt", "Palmer", "Robertson", "Black", "Holmes", "Stone", "Meyer",
        "Boyd", "Mills", "Warren", "Fox", "Rose", "Rice", "Moreno", "Schmidt", "Patel", "Ferguson", "Nichols",
        "Herrera", "Medina", "Ryan", "Fernandez", "Weaver", "Daniels", "Stephens", "Gardner", "Payne", "Kelley", "Dunn",
        "Pierce", "Arnold", "Tran", "Spencer", "Peters", "Hawkins", "Grant", "Hansen", "Castro", "Hoffman", "Hart",
        "Elliott", "Cunningham", "Knight", "Bradley", "Carroll", "Hudson", "Duncan", "Armstrong", "Berry", "Andrews",
        "Johnston", "Ray", "Lane", "Riley", "Carpenter", "Perkins", "Aguilar", "Silva", "Richards", "Willis",
        "Matthews", "Chapman", "Lawrence", "Garza", "Vargas", "Watkins", "Wheeler", "Larson", "Carlson", "Harper",
        "George", "Greene", "Burke", "Guzman", "Morrison", "Munoz", "Jacobs", "Obrien", "Lawson", "Franklin", "Lynch",
        "Bishop", "Carr", "Salazar", "Austin", "Mendez", "Gilbert", "Jensen", "Williamson", "Montgomery", "Harvey",
        "Oliver", "Howell", "Dean", "Hanson", "Weber", "Garrett", "Sims", "Burton", "Fuller", "Soto", "Mccoy", "Welch",
        "Chen", "Schultz", "Walters", "Reid", "Fields", "Walsh", "Little", "Fowler", "Bowman", "Davidson", "May", "Day",
        "Schneider", "Newman", "Brewer", "Lucas", "Holland", "Wong", "Banks", "Santos", "Curtis", "Pearson", "Delgado",
        "Valdez", "Pena", "Rios", "Douglas", "Sandoval", "Barrett", "Hopkins", "Keller", "Guerrero", "Stanley", "Bates",
        "Alvarado", "Beck", "Ortega", "Wade", "Estrada", "Contreras", "Barnett", "Caldwell", "Santiago", "Lambert",
        "Powers", "Chambers", "Nunez", "Craig", "Leonard", "Lowe", "Rhodes", "Byrd", "Gregory", "Shelton", "Frazier",
        "Becker", "Maldonado", "Fleming", "Vega", "Sutton", "Cohen", "Jennings", "Parks", "Mcdaniel", "Watts", "Barker",
        "Norris", "Vaughn", "Vazquez", "Holt", "Schwartz", "Steele", "Benson", "Neal", "Dominguez", "Horton", "Terry",
        "Wolfe", "Hale", "Lyons", "Graves", "Haynes", "Miles", "Park", "Warner", "Padilla", "Bush", "Thornton",
        "Mccarthy", "Mann", "Zimmerman", "Erickson", "Fletcher", "Mckinney", "Page", "Dawson", "Joseph", "Marquez",
        "Reeves", "Klein", "Espinoza", "Baldwin", "Moran", "Love", "Robbins", "Higgins", "Ball", "Cortez", "Le",
        "Griffith", "Bowen", "Sharp", "Cummings", "Ramsey", "Hardy", "Swanson", "Barber", "Acosta", "Luna", "Chandler",
        "Blair", "Daniel", "Cross", "Simon", "Dennis", "Oconnor", "Quinn", "Gross", "Navarro", "Moss", "Fitzgerald",
        "Doyle", "Mclaughlin", "Rojas", "Rodgers", "Stevenson", "Singh", "Yang", "Figueroa", "Harmon", "Newton", "Paul",
        "Manning", "Garner", "Mcgee", "Reese", "Francis", "Burgess", "Adkins", "Goodman", "Curry", "Brady",
        "Christensen", "Potter", "Walton", "Goodwin", "Mullins", "Molina", "Webster", "Fischer", "Campos", "Avila",
        "Sherman", "Todd", "Chang", "Blake", "Malone", "Wolf", "Hodges", "Juarez", "Gill", "Farmer", "Hines",
        "Gallagher", "Duran", "Hubbard", "Cannon", "Miranda", "Wang", "Saunders", "Tate", "Mack", "Hammond", "Carrillo",
        "Townsend", "Wise", "Ingram", "Barton", "Mejia", "Ayala", "Schroeder", "Hampton", "Rowe", "Parsons", "Frank",
        "Waters", "Strickland", "Osborne", "Maxwell", "Chan", "Deleon", "Norman", "Harrington", "Casey", "Patton",
        "Logan", "Bowers", "Mueller", "Glover", "Floyd", "Hartman", "Buchanan", "Cobb", "French", "Kramer", "Mccormick",
        "Clarke", "Tyler", "Gibbs", "Moody", "Conner", "Sparks", "Mcguire", "Leon", "Bauer", "Norton", "Pope", "Flynn",
        "Hogan", "Robles", "Salinas", "Yates", "Lindsey", "Lloyd", "Marsh", "Mcbride", "Owen", "Solis", "Pham", "Lang",
        "Pratt", "Lara", "Brock", "Ballard", "Trujillo", "Shaffer", "Drake", "Roman", "Aguirre", "Morton", "Stokes",
        "Lamb", "Pacheco", "Patrick", "Cochran", "Shepherd", "Cain", "Burnett", "Hess", "Li", "Cervantes", "Olsen",
        "Briggs", "Ochoa", "Cabrera", "Velasquez", "Montoya", "Roth", "Meyers", "Cardenas", "Fuentes", "Weiss",
        "Hoover", "Wilkins", "Nicholson", "Underwood", "Short", "Carson", "Morrow", "Colon", "Holloway", "Summers",
        "Bryan", "Petersen", "Mckenzie", "Serrano", "Wilcox", "Carey", "Clayton", "Poole", "Calderon", "Gallegos",
        "Greer", "Rivas", "Guerra", "Decker", "Collier", "Wall", "Whitaker", "Bass", "Flowers", "Davenport", "Conley",
        "Houston", "Huff", "Copeland", "Hood", "Monroe", "Massey", "Roberson", "Combs", "Franco", "Larsen", "Pittman",
        "Randall", "Skinner", "Wilkinson", "Kirby", "Cameron", "Bridges", "Anthony", "Richard", "Kirk", "Bruce",
        "Singleton", "Mathis", "Bradford", "Boone", "Abbott", "Charles", "Allison", "Sweeney", "Atkinson", "Horn",
        "Jefferson", "Rosales", "York", "Christian", "Phelps", "Farrell", "Castaneda", "Nash", "Dickerson", "Bond",
        "Wyatt", "Foley", "Chase", "Gates", "Vincent", "Mathews", "Hodge", "Garrison", "Trevino", "Villarreal", "Heath",
        "Dalton", "Valencia", "Callahan", "Hensley", "Atkins", "Huffman", "Roy", "Boyer", "Shields", "Lin", "Hancock",
        "Grimes", "Glenn", "Cline", "Delacruz", "Camacho", "Dillon", "Parrish", "Oneill", "Melton", "Booth", "Kane",
        "Berg", "Harrell", "Pitts", "Savage", "Wiggins", "Brennan", "Salas", "Marks", "Russo", "Sawyer", "Baxter",
        "Golden", "Hutchinson", "Liu", "Walter", "Mcdowell", "Wiley", "Rich", "Humphrey", "Johns", "Koch", "Suarez",
        "Hobbs", "Beard", "Gilmore", "Ibarra", "Keith", "Macias", "Khan", "Andrade", "Ware", "Stephenson", "Henson",
        "Wilkerson", "Dyer", "Mcclure", "Blackwell", "Mercado", "Tanner", "Eaton", "Clay", "Barron", "Beasley", "Oneal",
        "Preston", "Small", "Wu", "Zamora", "Macdonald", "Vance", "Snow", "Mcclain", "Stafford", "Orozco", "Barry",
        "English", "Shannon", "Kline", "Jacobson", "Woodard", "Huang", "Kemp", "Mosley", "Prince", "Merritt", "Hurst",
        "Villanueva", "Roach", "Nolan", "Lam", "Yoder", "Mccullough", "Lester", "Santana", "Valenzuela", "Winters",
        "Barrera", "Leach", "Orr", "Berger", "Mckee", "Strong", "Conway", "Stein", "Whitehead", "Bullock", "Escobar",
        "Knox", "Meadows", "Solomon", "Velez", "Odonnell", "Kerr", "Stout", "Blankenship", "Browning", "Kent", "Lozano",
        "Bartlett", "Pruitt", "Buck", "Barr", "Gaines", "Durham", "Gentry", "Mcintyre", "Sloan", "Melendez", "Rocha",
        "Herman", "Sexton", "Moon", "Hendricks", "Rangel", "Stark", "Lowery", "Hardin", "Hull", "Sellers", "Ellison",
        "Calhoun", "Gillespie", "Mora", "Knapp", "Mccall", "Morse", "Dorsey", "Weeks", "Nielsen", "Livingston",
        "Leblanc", "Mclean", "Bradshaw", "Glass", "Middleton", "Buckley", "Schaefer", "Frost", "Howe", "House",
        "Mcintosh", "Ho", "Pennington", "Reilly", "Hebert", "Mcfarland", "Hickman", "Noble", "Spears", "Conrad",
        "Arias", "Galvan", "Velazquez", "Huynh", "Frederick", "Randolph", "Cantu", "Fitzpatrick", "Mahoney", "Peck",
        "Villa", "Michael", "Donovan", "Mcconnell", "Walls", "Boyle", "Mayer", "Zuniga", "Giles", "Pineda", "Pace",
        "Hurley", "Mays", "Mcmillan", "Crosby", "Ayers", "Case", "Bentley", "Shepard", "Everett", "Pugh", "David",
        "Mcmahon", "Dunlap", "Bender", "Hahn", "Harding", "Acevedo", "Raymond", "Blackburn", "Duffy", "Landry",
        "Dougherty", "Bautista", "Shah", "Potts", "Arroyo", "Valentine", "Meza", "Gould", "Vaughan", "Fry", "Rush",
        "Avery", "Herring", "Dodson", "Clements", "Sampson", "Tapia", "Bean", "Lynn", "Crane", "Farley", "Cisneros",
        "Benton", "Ashley", "Mckay", "Finley", "Best", "Blevins", "Friedman", "Moses", "Sosa", "Blanchard", "Huber",
        "Frye", "Krueger", "Bernard", "Rosario", "Rubio", "Mullen", "Benjamin", "Haley", "Chung", "Moyer", "Choi",
        "Horne", "Yu", "Woodward", "Ali", "Nixon", "Hayden", "Rivers", "Estes", "Mccarty", "Richmond", "Stuart",
        "Maynard", "Brandt", "Oconnell", "Hanna", "Sanford", "Sheppard", "Church", "Burch", "Levy", "Rasmussen",
        "Coffey", "Ponce", "Faulkner", "Donaldson", "Schmitt", "Novak", "Costa", "Montes", "Booker", "Cordova",
        "Waller", "Arellano", "Maddox", "Mata", "Bonilla", "Stanton", "Compton", "Kaufman", "Dudley", "Mcpherson",
        "Beltran", "Dickson", "Mccann", "Villegas", "Proctor", "Hester", "Cantrell", "Daugherty", "Cherry", "Bray",
        "Davila", "Rowland", "Levine", "Madden", "Spence", "Good", "Irwin", "Werner", "Krause", "Petty", "Whitney",
        "Baird", "Hooper", "Pollard", "Zavala", "Jarvis", "Holden", "Haas", "Hendrix", "Mcgrath", "Bird", "Lucero",
        "Terrell", "Riggs", "Joyce", "Mercer", "Rollins", "Galloway", "Duke", "Odom", "Andersen", "Downs", "Hatfield",
        "Benitez", "Archer", "Huerta", "Travis", "Mcneil", "Hinton", "Zhang", "Hays", "Mayo", "Fritz", "Branch",
        "Mooney", "Ewing", "Ritter", "Esparza", "Frey", "Braun", "Gay", "Riddle", "Haney", "Kaiser", "Holder", "Chaney",
        "Mcknight", "Gamble", "Vang", "Cooley", "Carney", "Cowan", "Forbes", "Ferrell", "Davies", "Barajas", "Shea",
        "Osborn", "Bright", "Cuevas", "Bolton", "Murillo", "Lutz", "Duarte", "Kidd", "Key", "Cooke"]

GENDER = ["Male", "Female"]


def reg_user(request):
    print("POST http://app.follo.co.in/bollyapi/api/login/appregister HTTP/1.1")
    print("Content-Type: application/json; charset=utf-8")
    print("Host: app.follo.co.in")
    print("Connection: Keep-Alive")
    print("User-Agent: okhttp/3.2.0")
    print("Accept-Encoding: gzip")
    print("\n\n")

    model = random.choice(MANUFACTURER)
    sex = random.choice(GENDER)

    appmode = "AND"
    accesstoken = "EAACVuZCS6jj4BADUtrtR63785qnc9JiR4JZAVPx8Y73KAZAbRoURSztPuZBfFyawtspOPg0nwXb1X6IiE43FY7G0UBmEUdcQNqQiicoabfJLlYkEcXRelpciPPn5hPxhDTkmQS8bfCRIDqJswSpLYp1L7m5xgXh9O9ALJLkgzfZCWcO5wXBsHiPfiuhXpekatz2jsftwB9AZDZD"

    appversion = "1.1.9"
    handsettype = "xhdpi"
    osversion = "4.4.4"
    profileimage = "http://graph.facebook.com/100912613721916/picture?type=large"
    deviceid = random_generator(15, string.digits)
    # deviceid="986826084221544"
    mobileno = ""
    # socialid = random_generator(15,string.digits)
    socialid = "100912613721916"
    print(socialid)
    username = random.choice(NAME) + " " + random.choice(NAME)
    manufacture = random.choice(MANUFACTURER)
    email = random.choice(NAME) + random.choice(NAME) + random_generator(5, string.digits) + "@gmall.com"
    print(email)
    dob = ""
    tokenexpire = "Fri Dec 30 11:56:44 IST 2016"
    logintype = "FB"
    advid = random_generator(8) + "-" + random_generator(4) + "-" + random_generator(4) + "-" + random_generator(
        4) + "-" + random_generator(12)

    u = User(logintype=logintype, advid=advid, deviceid=deviceid, mobileno=mobileno, socialid=socialid,
             username=username, manufacture=manufacture, email=email, dob=dob, tokenexpire=tokenexpire, model=model,
             sex=sex, appmode=appmode, accesstoken=accesstoken, appversion=appversion, handsettype=handsettype,
             osversion=osversion, profileimage=profileimage)
    url = "http://app.follo.co.in/bollyapi/api/login/appregister"
    data = {
        "model": model,
        "sex": sex,
        "appmode": appmode,
        "accesstoken": accesstoken,
        "appversion": appversion,
        "handsettype": handsettype,
        "osversion": osversion,
        "profileimage": profileimage,
        "deviceid": deviceid,
        "mobileno": mobileno,
        "socialid": socialid,
        "username": username,
        "manufacture": manufacture,
        "email": email,
        "dob": dob,
        "tokenexpire": tokenexpire,
        "logintype": logintype,
        "advid": advid
    }

    print(data)
    headers = {'content-type': 'application/json; charset=utf-8',
               'connection': 'Keep-Alive',
               'host': 'app.follo.co.in',
               'user-agent': 'okhttp/3.2.0',
               'accept-encoding': 'gzip'}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(r.text)[0]
    print(json_data)
    if json_data['status'] == "OK":
        u.userid = int(json_data["userid"])
        print(u.userid)
        u.save()

    url1 = "http://app.follo.co.in/bollyapi/api/deviceregister/register"
    data1 = {
        "regid": "",
        "model": model,
        "uachannel": advid,
        "msisdn": deviceid,
        "servicename": "B20",
        "handsettype": handsettype,
        "osversion": osversion,
        "mode": appmode,
        "version": appversion,
        "source": "app",
        "isactive": "1",
        "manufacture": manufacture,
        "email": "",
        "dob": "",
        "name": "",
        "advid": advid
    }
    headers1 = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}

    r = requests.post(url1, data=json.dumps(data1), headers=headers1)
    json_data = json.loads(r.text)[0]
    print(json_data)
    users = User.objects.all()
    return HttpResponseRedirect(reverse('index'))




def index(request):
    #register_user()
    users = User.objects.all()
    return render(request, 'b20/index.html', {'users': users})


def allc(request):
    #register_user()
    users = User.objects.all()
    for u in users:
        print("*" * 20)
        print(u.userid)
        print("*" * 20)
        print("\n")
        print("---------------------------------Getting BMS quiz----------------------------------------\n")

        bmsquizb20(request=request, uid=u.userid)
        print("---------------------------------Getting Daily quiz----------------------------------------\n")

        q(uid=u.userid)
        print("---------------------------------Getting Coupon----------------------------------------\n")
        get_coupon(u.userid)
        print("---------------------------------Getting BMS Coupon----------------------------------------\n")

        get_bmscoupon(u.userid)

    coupons=AliveVoucher.objects.all()
    winpin=BMSVoucher.objects.all()
    return render(request, 'b20/all.html', {'coupons':coupons,'winpin':winpin})


def login(request):
    return render(request, 'b20/login.html', {})


def user_details(request, uid):
    u = get_object_or_404(User, userid=uid)
    get_coupon(uid)
    coupons=AliveVoucher.objects.filter(userid=u)
    print(list(coupons))
    print(u.userid)
    winpin = BMSVoucher.objects.all()
    print(list(winpin))
    return render(request, 'b20/user.html', {'user': u,'coupons':coupons,'winpin':winpin})


def get_coupon(uid):
    u = get_object_or_404(User, userid=uid)
    url1 = "http://app.follo.co.in/bollyapi/api/ChakDeVoucherList/getchakdevouchers"
    data1 = {
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "deviceid": u.deviceid
    }
    headers1 = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}

    r = requests.post(url1, data=json.dumps(data1), headers=headers1)
    json_data = json.loads(r.text)[0]
    print(json_data)
    if(json_data["status"]=="OK"):
        for c in json_data["coupon"]:
            AliveVoucher.objects.get_or_create(userid=u,couponcode=c["couponcode"],coupondate=c["coupondate"],expirydate=c["expirydate"])


def quizb20(request, uid):
    millis = int(round(time.time() * 1000))

    u = get_object_or_404(User, userid=uid)
    url1 = "http://app.follo.co.in/bollyapi/api/tnf/getquestions"

    data1 = {
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "celebid": "0",
        "deviceid": u.deviceid
    }
    headers1 = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}
    r = requests.post(url1, data=json.dumps(data1), headers=headers1)
    json_data = json.loads(r.text)[0]

    url = "http://app.follo.co.in/bollyapi/api/tnfuserresponse/answer"


    data = [{
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "deviceid": u.deviceid

    }]

    timetaken=0;

    print(millis)
    questions = []

    #print(json_data["question"])
    for j in json_data["question"]:
        #print(j)
        timetaken=timetaken+random.randint(2,4)
        q={"timeTaken": str(timetaken),
           "quizid": j["quizid"],
           "isattempt": "1",
           "points": j["points"],
           "sessionid": str(millis),
           "questionid": j["questionid"],
           "givenanswerid": j["answer"]
             }
        #print("++++++++++++++++++++++++++++++++++++++++\n")
        #print(q)
        questions.append(q)
    headers = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}

    data1 = [{"data":data,"questions":questions}]

    r = requests.post(url, data=json.dumps(data1), headers=headers)
   # json_data = json.loads(r.text)[0]
    #print(json_data)

    return HttpResponse(r.text)


def q(uid):
    millis = int(round(time.time() * 1000))
    
    u = get_object_or_404(User, userid=uid)
    url1 = "http://app.follo.co.in/bollyapi/api/tnf/getquestions"
    
    data1 = {
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "celebid": "0",
        "deviceid": u.deviceid
    }
    headers1 = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}
    r = requests.post(url1, data=json.dumps(data1), headers=headers1)
    json_data = json.loads(r.text)[0]
    
    url = "http://app.follo.co.in/bollyapi/api/tnfuserresponse/answer"
    
    
    data = [{
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "deviceid": u.deviceid
    
    }]
    
    timetaken=0;
    
    print(millis)
    questions = []
    
    #print(json_data["question"])
    for j in json_data["question"]:
        #print(j)
        timetaken=timetaken+random.randint(2,4)
        q={"timeTaken": str(timetaken),
           "quizid": j["quizid"],
           "isattempt": "1",
           "points": j["points"],
           "sessionid": str(millis),
           "questionid": j["questionid"],
           "givenanswerid": j["answer"]
             }
        #print("++++++++++++++++++++++++++++++++++++++++\n")
        #print(q)
        questions.append(q)
    headers = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}
    
    data1 = [{"data":data,"questions":questions}]
    
    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print((r.text).encode("utf-8"))







def bmsquizb20(request, uid):
    millis = int(round(time.time() * 1000))

    u = get_object_or_404(User, userid=uid)
    url1 = "http://app.follo.co.in/bollyapi/api/quizcard/getquestions"

    data1 = {
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "celebid": "0",
        "deviceid": u.deviceid
    }
    headers1 = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}
    r = requests.post(url1, data=json.dumps(data1), headers=headers1)
    json_data = json.loads(r.text)[0]

    url = "http://app.follo.co.in/bollyapi/api/userresponse/answer"


    data = [{
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "deviceid": u.deviceid

    }]

    ts=0;

    print(millis)
    questions = []

    #print(json_data["question"])
    for j in json_data["question"]:
        #print(j)
        ts=ts+1
        q={"timeTaken": str(random.randint(2,8)),
           "totalques": "10",
           "quizid": j["quizid"],
           "totalquesattempt": "10",
           "isattempt": "1",
           "totalscore": str(ts),
           "points": j["points"],
           "sessionid": str(millis),
           "questionid": j["questionid"],
           "givenanswerid": j["answer"]
             }
        #print("++++++++++++++++++++++++++++++++++++++++\n")
        #print(q)
        questions.append(q)
    headers = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}

    data1 = [{"data":data,"questions":questions}]

    r = requests.post(url, data=json.dumps(data1), headers=headers)
    print((r.text).encode("utf-8"))

def get_bmscoupon(uid):
    u = get_object_or_404(User, userid=uid)
    url1 = "http://app.follo.co.in/bollyapi/api/FFFVoucherList/getfffvouchers"
    data1 = {
        "model": u.model,
        "appmode": u.appmode,
        "manufacture": u.manufacture,
        "email": u.email,
        "userid": u.userid,
        "appversion": u.appversion,
        "handsettype": u.handsettype,
        "advid": u.advid,
        "osversion": u.osversion,
        "deviceid": u.deviceid
    }
    headers1 = {'content-type': 'application/json; charset=utf-8',
                'connection': 'Keep-Alive',
                'host': 'app.follo.co.in',
                'user-agent': 'okhttp/3.2.0',
                'accept-encoding': 'gzip'}

    r = requests.post(url1, data=json.dumps(data1), headers=headers1)
    json_data = json.loads(r.text)[0]
    print(json_data)
    if(json_data["status"]=="OK"):
        for c in json_data["coupon"]:
            BMSVoucher.objects.get_or_create(userid=u,couponcode=c["couponcode"],coupondate=c["coupondate"],expirydate=c["expirydate"])

