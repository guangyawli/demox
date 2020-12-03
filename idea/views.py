from django.shortcuts import render, redirect

# from .forms import TeamDataForm, TeamMember, TeamMemberForm, AddTeamMemberForm, TeamFilesForm
# from .models import Team
# from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'idea/index.html', locals())

