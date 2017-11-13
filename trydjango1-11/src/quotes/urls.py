from django.conf.urls import url
from django.contrib import admin




from .views import (
	QuoteCreateView,
	QuoteDetailView,
	QuoteListView
)

urlpatterns = [
    url(r'^$', QuoteListView.as_view(), name='list'),
    url(r'^create/$', QuoteCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', QuoteDetailView.as_view(), name='detail'),
]
