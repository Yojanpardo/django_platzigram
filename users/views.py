#django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
#forms
from .forms import ProfileForm, SignUpForm

#models
from django.contrib.auth.models import User
from posts.models import Post

# Create your views here.

def login_view(request):
    if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user =  authenticate(request, username=username, password=password)
	    if user:
	    	login(request,user)
	    	return redirect('posts:posts')
	    else:
	    	return render(request, 'users/login.html', {'error':'Nombre de usuario o contraseña invalidos'})
    return render(request,'users/login.html')

def sign_up_view(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('users:login')
	else:
		form = SignUpForm()
	return render(
		request = request,
		template_name = 'users/sign_up.html',
		context = {'form':form}
	)


@login_required
def edit_user(request):
	profile = request.user.profile
	
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			profile.website = data['website']
			profile.bio = data['bio']
			profile.phone_number = data['phone_number']
			profile.picture = data['picture']
			profile.save()
			
			url = reverse('users:detail',kwargs={'username':request.user.username})
			return redirect(url)

	else:
		form = ProfileForm()

	return render(
		request=request,
		template_name='users/edit_user.html',
		context={
			'profile':profile,
			'user':request.user,
			'form':form
		}
	)

@login_required
def logout_view(request):
	logout(request)
	return redirect('users:login')

class UserDetailView(LoginRequiredMixin, DetailView):
	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    user = self.get_object()
	    context['posts'] = Post.objects.filter(user=user).order_by('-created')
	    return context