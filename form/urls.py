from django.conf.urls import  *
from form import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$',views.login, name = 'login'),#Url for login user
    url(r'^login/',views.login, name = 'login'),#Url for login user
    url(r'^register/',views.register, name = 'register' ),#Url for register user
    url(r'^index/',views.index, name = 'index' ),#Url for Home
]
