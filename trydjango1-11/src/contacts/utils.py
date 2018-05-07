import random
import string
from twilio.rest import Client
import sys
import schedule
import datetime




from django.utils.text import slugify
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

account_sid = ""
auth_token = ""
my_twilio = "+1(201) 552-4734"
welcome_message = "welcome my name is Ellie and im here to inspire!"
test_message = "you did it"

contacts_to_message = {}

client = Client(account_sid, auth_token)


def send_welcome_message(**kwargs):
    message = client.api.account.messages.create(**kwargs)


def send_qoute_to_multi_contacts():
    q = UserContacts.objects.values('phone')
    for phone in q:
        print('doing')
        message = client.messages.create(to=phone, from_=my_twilio, 
                            body=welcome_message)

schedule.every().day.at("21:14").do(send_qoute_to_multi_contacts)


DONT_USE =['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


