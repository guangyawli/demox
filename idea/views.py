from django.shortcuts import render, redirect

from .forms import TeamDataForm, MemberTempForm
from .models import Team, MemberTemp
# from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'idea/index.html', locals())


def file_list(request):
    # 隊長編輯
    check_team = Team.objects.filter(leader=request.user).exists()
    if check_team:
        target_team = Team.objects.get(leader=request.user)
        if target_team.readme and target_team.video_link and target_team.affidavit:
            files = target_team
        else:
            files = None
    else:
        files = None

    return render(request, 'idea/file_list.html', {'files': files})


def team_data_modify(request):
    check_team = Team.objects.filter(leader=request.user)
    if check_team.exists():
        # 修改資料
        target_team = Team.objects.get(leader=request.user)
        target_mem1 = MemberTemp.objects.get(team__team_name=target_team.team_name)
        if request.method == "POST":
            form = TeamDataForm(request.POST, request.FILES, instance=target_team)
            mem1 = MemberTempForm(request.POST, instance=target_mem1)
            if form.is_valid() and mem1.is_valid():
                tmp = form.save(commit=False)
                form.save()
                t1 = mem1.save(commit=False)
                t1.team = tmp
                t1.save()
                return redirect("team_data_modify")
            else:
                print('!!!! error !!!')
        else:
            form = TeamDataForm(instance=target_team)
            mem1 = MemberTempForm(instance=target_mem1)
    else:
        # 新增資料
        if request.method == "POST":
            form = TeamDataForm(request.POST, request.FILES)
            mem1 = MemberTempForm(request.POST)
            if form.is_valid() and mem1.is_valid():
                tmp = form.save(commit=False)
                form.save()
                t1 = mem1.save(commit=False)
                t1.team = tmp
                t1.save()
                return redirect("team_data_modify")
            else:
                print('!!!! error !!!')
        else:
            form = TeamDataForm(initial={'leader': request.user})
            mem1 = MemberTempForm()

    return render(request, 'accounts/profile.html', locals())

