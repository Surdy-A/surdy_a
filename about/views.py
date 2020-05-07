from django.shortcuts import render
from .models import Contact
from sody_A.settings import BASE_DIR
from .models import Contact
from django.views.generic import ListView

class ContactList(ListView):
    print('BASE DIR'+ BASE_DIR)
    model = Contact
    template_name = 'home.html'