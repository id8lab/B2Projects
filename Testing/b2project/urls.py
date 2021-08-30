from django.urls import path
from . import views


# All Webpages links here 
urlpatterns = [
    path ('', views.index, name='index'),                #link to index html 
    path('register', views.register, name='register'),   #link to register html
    path('login', views.login, name='login'),            #link to login html
    path('logout', views.logout, name='logout')          #link to Logout    
    
]

