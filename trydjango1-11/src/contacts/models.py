from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse


from .utils import unique_slug_generator, account_sid, auth_token, client, my_twilio, welcome_message,send_welcome_message
from .validators import validate_timezone, is_valid_number


class UserContacts(models.Model):
	
	name	 	= models.CharField(max_length=120)
	phone 	 	= models.IntegerField(max_length=20, validators=[is_valid_number])
	location 	= models.CharField(max_length=120, null=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	slug 		= models.SlugField(null=True, blank=True)
	time_zone 	= models.CharField(max_length=120, validators=[validate_timezone])

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return f'/contact-detail/{self.slug}'
		return reverse('contacts:detail', kwargs={'slug': self.slug})


	
	@property 
	def title(self):
		return self.name # allows us to say obj.title

	class Meta:
		verbose_name = 'User Contact'
		verbose_name_plural ='User Contacts'
	
def uc_pre_save_reciever(sender, instance, *args, **kwargs):
	instance.time_zone = instance.time_zone.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


def uc_post_save_reciever(sender, instance, created, *args, **kwargs):
	print('saved')
	print(instance.name)
	cell = instance.phone
	welcome_data = {
		'to': cell, 
		'from_': my_twilio, 
		'body': welcome_message
	}
	send_welcome_message(**welcome_data)
	print(cell)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()

	
pre_save.connect(uc_pre_save_reciever, sender=UserContacts)

post_save.connect(uc_post_save_reciever, sender=UserContacts)

	
