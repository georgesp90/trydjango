import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#  function based view
def home(request):
	num = None
	some_list = [
		random.randint(0,10000000),
		random.randint(0,10000000),
		random.randint(0,10000000)
	]
	conditional_bool_item = False
	if conditional_bool_item:
		num = random.randint(0,10000000)
	context = {
		"num": num,
		"some_list": some_list
	}
	return render(request, "home.html", context) #response

def about(request):
	context = {
	}
	return render(request, "about.html", context) #response


def contact(request):
	context = {
	}
	return render(request, "contact.html", context) #response