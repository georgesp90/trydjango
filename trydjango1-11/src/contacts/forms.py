from django import forms


class ContactCreateForm(forms.Form):
	name	 	= forms.CharField()
	phone 	 	= forms.CharField()
	location 	= forms.CharField()