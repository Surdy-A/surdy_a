from django.shortcuts import render
from . import views
from .models import Project

def project_list(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'portfolio.html', context)


def project_detail(request, id):
    project = Project.objects.get(id=id)

    return render(request, 'portfolio_detail.html', {'project': project})
