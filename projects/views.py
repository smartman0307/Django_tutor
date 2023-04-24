from django.shortcuts import render
from projects.models import Project


# Create your views here.
def Project_index(request):
    projects = Project.objects.all()
    context = {"project": projects}

    return render(request, "project_index.html", context)


def Project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}

    return render(request, "project_detail.html", context)
