from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ContactCreateForm, UserContactsCreateForm
from .models import UserContacts


def contact_create_view(request):
	form = UserContactsCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save() 
			return HttpResponseRedirect('/contacts_list/')
		else:
			return HttpResponseRedirect('/login/')
	if form.errors: 
		errors = form.errors
			
	template_name = 'contacts/contacts_list_form.html'
	context = {"form": form, "errors": errors}
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

class UserContactsCreateView(CreateView):
	form_class = UserContactsCreateForm
	template_name = 'contacts/contacts_list_form.html'
	success_url = '/contacts_list/'

