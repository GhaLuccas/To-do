from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# accounts app  views here.

class UserCreateView(View):

    def get(self , request):
        form = UserCreationForm()
        return render(request , 'register.html' , {'form':form})
    
    def post(self ,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request , f'account created for {user.username}')
            login(request , user)
            return redirect('task:home')
        return render(request , 'register.html' , {'form':form})
    

class LoginView(View):

    def get(self , request):
        return render(request , 'login.html')

    def post(self , request):
        username= request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            messages.success(request , f'Welcome back {user.username}')
            return redirect('task:task') 
        else:
            messages.error(request , "Invalid username or password")
            return render(request , 'login.html')   


class LogoutView(View):

    def get(self , request):
        logout(request)
        messages.success(request , "You have been Logged out successfully")
        return redirect('task:home')