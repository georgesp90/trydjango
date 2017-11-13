from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import QuoteForm
from .models import Quote


class QuoteListView(ListView):
	def get_queryset(self):
		return Quote.objects.filter(user=self.request.user)


class QuoteDetailView (DetailView):
	def get_queryset(self):
		return Quote.objects.filter(user=self.request.user)


class QuoteCreateView(CreateView):
	def get_queryset(self):
		return Quote.objects.filter(user=self.request.user)

class QuoteUpdateView(UpdateView):
	def get_queryset(self):
		return Quote.objects.filter(user=self.request.user)