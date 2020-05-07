from django.urls import path
from .views import project_list, project_detail

urlpatterns = [
    path('portfolio', project_list, name = 'portfolio' ),
    path('portfolio/<int:id>', project_detail, name = 'project' )
]