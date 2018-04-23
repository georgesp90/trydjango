from django.core.exceptions import ValidationError
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Your Account Sid and Auth Token from twilio.com/user/account
# Store them in the environment variables:
# "TWILIO_ACCOUNT_SID" and "TWILIO_AUTH_TOKEN"
account_sid = "ACbbbd9efe355a2376772ffcf060f6794a"
auth_token = "c025f7bb1a54431e67824b107bca44a9"
client = Client(account_sid, auth_token)

def is_valid_number(value):
    try:
        response = client.lookups.phone_numbers(value).fetch(type="carrier")
        return True
    except TwilioRestException as e:
        if e.code in [20404, 21211]:
        	raise ValidationError(f'{value} is not a valid number')
        else:
        	raise ValidationError(f'{value} is not a valid number')

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def clean_email(self):
	email = value
	if ".edu" in email:
		raise forms.ValidationError('We do not accept edu emails ')


TIMEZONES = ['Alaskan', 'Central', 'Eastern', 'Hawaiian', 'Pacific', 'Mountain']

def validate_timezone(value):
	list_tz =[tz for tz in TIMEZONES]
	cap  = value.capitalize()
	if not value in TIMEZONES and not cap in TIMEZONES:
		raise ValidationError(f'{value} is not a valid timezone'
		' please enter valid US timezone:' + str(list_tz))
