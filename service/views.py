from django.shortcuts import render
from .models import About, Contact
# Create your views here.
from django.views.generic import ListView

class AboutListView(ListView):
    model = About
    template_name = 'about.html'

class ContactListView(ListView):
    model = Contact
    template_name = 'contact.html'

