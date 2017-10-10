from django.core.exceptions import ValidationError


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
