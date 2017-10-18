from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse


from .utils import unique_slug_generator
from .validators import validate_timezone

User = settings.AUTH_USER_MODEL

class UserContacts(models.Model):
	owner 		= models.ForeignKey(User)
	name	 	= models.CharField(max_length=120)
	phone 	 	= models.CharField(max_length=9, null=True, blank=True)
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


# def uc_post_save_reciever(sender, instance, created, *args, **kwargs):
# 	print('saved')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()

	
pre_save.connect(uc_pre_save_reciever, sender=UserContacts)

# post_save.connect(uc_post_save_reciever, sender=UserContacts)

	
