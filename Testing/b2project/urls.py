from django.urls import path
from . import views


# All Webpages links here 
urlpatterns = [
    path ('', views.index, name='index'),                #link to index html 
    path('register', views.register, name='register'),   #link to register html
    path('login', views.login, name='login'),            #link to login html
    path('logout', views.logout, name='logout'),         #link to Logout    
    path('createcontract', views.createcontract, name='createcontract'), #link to createcontract.html
    path('joblists', views.joblists, name='joblists'),   #link to joblists.html
    path('contracts', views.contracts, name='contracts'),#link to contracts.html
    path('userprofile', views.userprofile, name='userprofile'),     #link to userprofile.html
]

