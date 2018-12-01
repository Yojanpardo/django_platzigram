#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#models
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def login_view(request):
    if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user =  authenticate(request, username=username, password=password)
	    if user:
	    	login(request,user)
	    	return redirect('posts')
	    else:
	    	return render(request, 'users/login.html', {'error':'Nombre de usuario o contraseña invalidos'})
    return render(request,'users/login.html')

def sign_up_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_c = request.POST['password_c']
		#import pdb; pdb.set_trace() #esta linea permite hacer un debug delicioso
		if password == password_c:
			user = User.objects.create_user(username=username,password=password)
			user.first_name = request.POST['firstname']
			user.last_name = request.POST['lastname']
			user.email = request.POST['email']

			profile = Profile(user=user)
			profile.save()

			return redirect('login')
		else:
			return render(request, 'users/sign_up.html', {'confirmation_error':'Las contraseñas escritas no coinciden'})
	return render(request, 'users/sign_up.html')

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')