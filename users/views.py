from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method=='POST':
        print('='*10)

        print('='*10)
    return render(request,'users/login.html')
