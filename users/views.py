from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    print(username,': ',password)
	    user =  authenticate(request, username=username, password=password)
	    if user:
	    	login(request,user)
	    	return redirect('posts')
	    else:
	    	return render(request, 'users/login.html', {'error':'Nombre de usuario o contraseña invalidos'})
    return render(request,'users/login.html')

def sign_up_view(request):
	return render(request, 'users/sign_up.html')

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')