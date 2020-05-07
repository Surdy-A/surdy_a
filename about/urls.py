from django.urls import path

from .views import  ContactList

urlpatterns = [
    path('', ContactList.as_view()),
    #path('', ListContact.as_view()),
]