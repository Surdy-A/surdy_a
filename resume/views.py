from django.shortcuts import render
from .models import *
from django.views.generic import ListView

class EducationListView(ListView):
    model = Education
    template_name = 'resume.html'

class ExperienceListView(ListView):
    model = Experience 
    template_name = 'resume.html'


class EducationListView(ListView):
    model = Skills
    template_name = 'resume.html'

def resumeView(request):
    education = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skills.objects.all()
    certificates = Certificate.objects.all()
    
    context = {
        'education': education,
        'experiences': experiences,
        'skills': skills,
        'certificates':certificates
    }

    return render(request, 'resume.html', context)
