from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.Form):
	username = forms.CharField(min_length=4, max_length=40)
	
	password = forms.CharField(min_length=8, widget=forms.PasswordInput())
	password_c = forms.CharField(min_length=8, widget=forms.PasswordInput())

	first_name = forms.CharField(min_length=4)
	last_name = forms.CharField(min_length=4)

	email = forms.CharField(min_length=6,max_length=60,widget=forms.EmailInput())

	def clean_username(self):
		username = self.cleaned_data['username']
		username_exist = User.objects.filter(username=username).exists()
		if username_exist:
			raise forms.ValidationError('username is already in use')
		return username

	def clean(self):
		#verifica la confirmacion del password
		data = super().clean()
		password = data['password']
		password_c = data['password_c']

		if password != password_c:
			raise forms.ValidationError('Password confirmation do not match.')
		return data

	def save(self):
		data = self.cleaned_data
		data.pop('password_c')

		user = User.objects.create_user(**data)
		profile = Profile(user=user)
		profile.save()
	

class ProfileForm(forms.Form):
	website = forms.URLField(max_length=100	, required=True)
	phone_number = forms.CharField(max_length=20, required=False)
	bio = forms.CharField(max_length=255,required=True)
	picture = forms.ImageField()