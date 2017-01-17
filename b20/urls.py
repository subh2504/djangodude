from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<uid>\d+)/$', views.user_details, name='user_details'),
    url(r'^quizb20/(?P<uid>\d+)/$', views.quizb20, name='quizb20'),
    url(r'^bmsquizb20/(?P<uid>\d+)/$', views.bmsquizb20, name='bmsquizb20'),
    url(r'^konnect/(?P<uid>\d+)/$', views.konnect, name='konnect'),
    url(r'^reg_user/$', views.reg_user, name='reg_user'),
    url(r'^submit_mob/$', views.submit_mob, name='submit_mob'),
    url(r'^submit_otp/$', views.submit_otp, name='submit_otp'),
    url(r'^all/$', views.allc, name='all'),
]