from django import forms
from .models import UserContacts 
from .validators import validate_timezone



class ContactCreateForm(forms.Form):
	name	 	= forms.CharField()
	phone 	 	= forms.IntegerField(required=True)
	location 	= forms.CharField(required=False)
	time_zone   = forms.CharField()

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == 'Hello':
			raise forms.ValidationError('Not a valid name')
		return name


class UserContactsCreateForm(forms.ModelForm):
	# email 		= forms.EmailField(required=False)
	# time_zone   = forms.CharField(validators=[validate_timezone])
	class Meta:
		model = UserContacts
		fields =[
			'name',
			'phone'
		]

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == 'Hello':
			raise forms.ValidationError('Not a valid name')
		return name

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if ".edu" in email:
	# 		raise forms.ValidationError('We do not accept edu emails ')
	# 	return email
