from django.urls import path

#from .views import BlogListView, BlogDetailView
from . import views
from .views import  AboutListView, ContactListView

app_name =  'service'
urlpatterns = [
    path('about', AboutListView.as_view(), name='about'),
    path('contact/', ContactListView.as_view(), name='contact')
    #path('', ListContact.as_view()),
]