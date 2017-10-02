from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import UserContacts

def contacts_list_view(request):
	template_name = 'contacts/contacts_list.html'
	queryset = UserContacts.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

