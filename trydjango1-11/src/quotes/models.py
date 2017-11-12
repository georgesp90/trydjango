from django.conf import settings
from django.db import models

from contacts.models import UserContacts
from django import forms



class Quote(models.Model):
	# choices
	motivational 	= 'MOT'
	spiritual	 	= 'SPR'
	funny			= 'LOL'
	TYPE_OF_QUOTE			= (
			(motivational, 'motivational'),
			(spiritual, 'spiritual'),
			(funny, 'funny'),
	)
	# associations
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL)
	contact 			= models.ForeignKey(UserContacts)
	# quote type 
	quote_type			= models.CharField(max_length=3, choices=TYPE_OF_QUOTE,)
	postscript 			= models.TextField(blank=True, null=True)
	public 				= models.BooleanField(default=True)
	
	timestamp 			= models.DateTimeField(auto_now_add=True)
	updated 			= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated', '-timestamp'] # gives the lastest when you do Quote.objects.all()
