from django import forms
from .models import UserContacts 



class ContactCreateForm(forms.Form):
	name	 	= forms.CharField()
	phone 	 	= forms.CharField(required=False)
	location 	= forms.CharField(required=False)

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == 'Hello':
			raise forms.ValidationError('Not a valid name')
		return name


class UserContactsCreateForm(forms.ModelForm):
	class Meta:
		model = UserContacts
		fields =[
			'name',
			'phone',
			'location'
		]

