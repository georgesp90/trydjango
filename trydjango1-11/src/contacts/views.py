from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import UserContacts

def contacts_list_view(request):
	template_name = 'contacts/contacts_list.html'
	queryset = UserContacts.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)


class ContactsListView(ListView):
	
	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = UserContacts.objects.filter(
					Q(location__iexact=slug) |
					Q(location__icontains=slug) # you should remove this if you wanna do state abbrevations
				)
		else:
			queryset = UserContacts.objects.all()
		return queryset

