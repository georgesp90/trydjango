from django.db import models

# Create your models here.
class UserContacts(models.Model):
	name	 	= models.CharField(max_length=120)
	phone 	 	= models.CharField(max_length=9, null=True, blank=False)
	location 	= models.CharField(max_length=120, null=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'User Contact'
		verbose_name_plural ='User Contacts'