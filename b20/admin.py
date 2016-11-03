from django.contrib import admin
from .models import BMSVoucher,AliveVoucher,User

# Register your models here.
admin.site.register(BMSVoucher)
admin.site.register(AliveVoucher)
admin.site.register(User)