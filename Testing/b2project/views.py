from django.shortcuts import render, redirect   #Redirect the user to another page
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Feature   #Importing Feature here from models.py

# Create your views here.   
# ALL Main Things happen here  

# whatever we do inside this function, pass to url_list inside urls.py
#Backend 

def index(request):

    return render (request, 'index.html')


#Register Function 
def register(request):
    #Getting data from register html Form and these data will store into database
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passowrd2 = request.POST['password2']

        if(password == passowrd2):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already existed')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is alredy existed')
                return redirect('register')
            
            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        #IF two password are not the same while creating 
        else: 
            messages.info(request, 'Passowrd is not matched')
            return redirect('register')

    #If method is not POST
    else:
        return render (request, 'register.html')


#Login Function 
def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        #IF user data is on our database
        if user is not None:
            auth.login(request, user)
            return redirect('/')  #redirect the user to our main page
        
        #If user is not on our database 
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('login')

    return render(request, 'login.html')

#Logout Function 
def logout(request):
    auth.logout(request)
    return redirect('/') # redirect to Home page

def createcontract(request):
    
    return render(request, 'createcontract.html')

def joblists(request):

    return render(request, 'joblists.html')

def contracts(request):

    return render(request, 'contracts.html')

def userprofile(request):

    return render(request, 'userprofile.html')






