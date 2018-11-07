from django import forms
from .models import UserContacts 
from .validators import validate_timezone



class UserContactsCreateForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(
	    attrs={
	        'class': 'form-group',
	        'placeholder': 'Name'
	    }
	))

	phone = forms.CharField(widget=forms.TextInput(
	    attrs={
	        'class': 'form-group',
	        'placeholder': 'Phone'
	    }
	))
		
	class Meta:
		model = UserContacts
		fields =[
			'name',
			'phone'
		]

	def clean_phone(self):
		phone = self.cleaned_data.get("phone")
		qs = UserContacts.objects.filter(phone__iexact=phone)
		if qs.exists():
			raise forms.ValidationError('Phone Number already registered')
		return phone
