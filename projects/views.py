from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'projects/index.html', locals())


def rated_projects(request):
    return render(request, 'projects/rated-projects.html', locals())
