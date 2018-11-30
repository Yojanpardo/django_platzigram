from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
