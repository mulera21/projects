from django.shortcuts import render

# Create your views here.

from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = project.objects.get(pk=pl)
    context = {
        "project": project
    }
    return render(request, 'projects/project_detail.html', context)
