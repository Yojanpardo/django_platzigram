from django import forms

class ProfileForm(forms.Form):
	website = forms.URLField(max_length=100	, required=True)
	phone_number = forms.CharField(max_length=20, required=False)
	bio = forms.CharField(max_length=255,required=True)
	picture = forms.ImageField()