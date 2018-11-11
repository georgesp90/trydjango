from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView




from .views import (
	# contact_create_view,
	# contacts_list_view,
	ContactsListView,
	ContactsDetailView,
	UserContactsCreateView
)

urlpatterns = [
    url(r'^list$', ContactsListView.as_view(), name='list'),
    url(r'^$', UserContactsCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ContactsDetailView.as_view(), name='detail'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
