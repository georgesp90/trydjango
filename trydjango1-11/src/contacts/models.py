from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

# Create your models here.
class UserContacts(models.Model):
	name	 	= models.CharField(max_length=120)
	phone 	 	= models.CharField(max_length=9, null=True, blank=False)
	location 	= models.CharField(max_length=120, null=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	slug 		= models.SlugField(null=True, blank=False)

	def __str__(self):
		return self.name

	
	@property 
	def title(self):
		return self.name # allows us to say obj.title

	class Meta:
		verbose_name = 'User Contact'
		verbose_name_plural ='User Contacts'
	
def uc_pre_save_reciever(sender, instance, *args, **kwargs):
	print('saving..')
	print(instance.timestamp)
	# if not instance.slug:
	# 	instance.slug = unique_slug_generator(instance)
	# 	instance.save()


def uc_post_save_reciever(sender, instance, created, *args, **kwargs):
	print('saved')
	print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()

	
pre_save.connect(uc_pre_save_reciever, sender=UserContacts)

post_save.connect(uc_post_save_reciever, sender=UserContacts)

	
