from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import UserContacts
from .forms import ContactCreateForm


def contact_create_view(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		pnone = request.POST.get('pnone')
		location = request.POST.get('location')
		obj = UserContacts.objects.create(
				name = name,
				phone = pnone,
				location = location
			)
		return HttpResponseRedirect('/contacts_list/')
	template_name = 'contacts/contacts_list_form.html'
	context = {}
	return render(request, template_name, context) 


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


class ContactsDetailView(DetailView):
	queryset = UserContacts.objects.all() #filter(location__iexact='nys') #filer it by user

	# def get_object(self, *args, **kwargs):
	# 	cont_id = self.kwargs.get('cont_id')
	# 	obj =  get_object_or_404(UserContacts, id=cont_id)
	# 	return obj
	#  