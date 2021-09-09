from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


# All Webpages links here 
urlpatterns = [
    path ('', views.index, name='index'),                #link to index html 
    path('register', views.register, name='register'),   #link to register html
    path('login', views.login, name='login'),            #link to login html
    path('logout', views.logout, name='logout'),         #link to Logout    
    path('createcontract', views.createcontract, name='createcontract'), #link to createcontract.html
    path('contracts', views.contracts, name='contracts'),   #link to contracts.html
    path('userprofile', views.userprofile, name='userprofile'),     #link to userprofile.html
    path('joblists', views.jobLists, name='joblists'), #link to jobLists.html
    path('salarystatement', views.salarystatement, name = 'salarystatement'),  # link to salarystatement.html
    path('image_upload', image_upload_view, name = "image upload"),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)