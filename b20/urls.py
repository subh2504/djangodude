from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<uid>\d+)/$', views.user_details, name='user_details'),
    url(r'^quizb20/(?P<uid>\d+)/$', views.quizb20, name='quizb20'),
]