from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=20,blank=True, null=True)
    sex = models.CharField(max_length=8,
        choices=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    ),blank=True, null=True)
    appmode = models.CharField(max_length=10,default="AND")
    accesstoken = models.TextField(default="EAACVuZCS6jj4BAKaCynep1cdIdzjAIP9p4vRPxJQ5ZBxRvuvscUqiapCOmEMDuWjH5fce5hOs5NIg2XCPu4iMM8bkvm3Pqn6OfIGdrggmTm3jObcWRSOwIGZCGZBkJZAkwVBVLBOhcOPG6xARjghVnf2Czt5MZBOaXJnyAy5Leh5OAL7qvKsInHiVX3LV5Jsv9ZCcVdED7DLrxvgNpIJXfQ")
    appversion = models.CharField(max_length=10)
    handsettype = models.CharField(max_length=10)
    osversion = models.CharField(max_length=10)
    profileimage = models.URLField()
    deviceid = models.CharField(max_length=20)
    mobileno = models.CharField(max_length=12,blank=True, null=True)
    socialid = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    manufacture = models.CharField(max_length=30)
    email = models.EmailField()
    dob = models.CharField(max_length=12,blank=True, null=True)
    tokenexpire = models.CharField(max_length=55)
    logintype = models.CharField(default="FB",max_length=20)
    advid = models.CharField(max_length=40)
    createdate = models.DateTimeField(default=timezone.now)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.userid)


class AliveVoucher(models.Model):
    userid = models.ForeignKey("User")
    couponcode=models.TextField(unique=True)
    coupondate=models.DateField(null=True)
    expirydate=models.DateField(null=True)
    used=models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.couponcode


class BMSVoucher(models.Model):
    userid = models.ForeignKey("User")
    couponcode=models.TextField(unique=True)
    coupondate=models.CharField(null=True,max_length=20)
    expirydate=models.CharField(null=True,max_length=20)
    used=models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.couponcode