from django.urls import path
from . views import resumeView
app_name = 'resume'
urlpatterns = [
    path('resume/',  resumeView, name='resume'),
]