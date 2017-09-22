from django.conf.urls import  *
from form import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$',views.login, name = 'login'),#Url for login user
    url(r'^login/',views.login, name = 'login'),#Url for login user
    url(r'^logout/',views.logout, name = 'logout'),#Url for login user
    url(r'^register/',views.register, name = 'register' ),#Url for register user
    url(r'^index/',views.index, name = 'index' ),#Url for Home
    url(r'^viewform/',views.viewform, name = 'viewform' ),#Url for Home
]
