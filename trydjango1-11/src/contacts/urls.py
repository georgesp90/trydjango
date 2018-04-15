from django.conf.urls import url
from django.contrib import admin




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
]
