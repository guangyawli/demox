from django.shortcuts import render, redirect

from .forms import TeamDataForm, TeamMember, TeamMemberForm, AddTeamMemberForm, TeamFilesForm
from .models import Team
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


def show_team(request):
    check_team = Team.objects.filter(leader=request.user)
    if check_team.exists():
        if request.method == "GET":
            target_team = Team.objects.get(leader=request.user)
            target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
            form = TeamDataForm(instance=target_team)
            real_member_num = target_members.count()
            if real_member_num == 0:
                error_message = 'no member'
        else:
            error_message = 'request.method POST'

    else:
        return redirect('add_team')

    return render(request, 'idea/show_team.html', locals())


def add_team(request):
    check_team = Team.objects.filter(leader=request.user)
    if check_team:
        error_message = 'Team is exist'
        return redirect('show_team')

    if request.method == "POST":
        form = TeamDataForm(request.POST, request.FILES)
        mem1 = TeamMemberForm(request.POST)

        if form.is_valid() and mem1.is_valid():
            tmp = form.save(commit=False)
            form.save()
            t1 = mem1.save(commit=False)
            t1.team = tmp
            t1.save()
            # 回傳並顯示
            target_team = Team.objects.get(leader=request.user)
            target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
            error_message = '隊伍新增成功'
            form = TeamDataForm(instance=target_team)
            real_member_num = target_members.count()
            return render(request, 'idea/show_team.html', locals())
        else:
            print('!!!! error !!!')
            error_message = mem1.errors
    else:
        form = TeamDataForm(initial={'leader': request.user})
        mem1 = TeamMemberForm()

    return render(request, 'idea/add_team.html', locals())


def modify_team(request):
    check_team = Team.objects.filter(leader=request.user)
    target_team = Team.objects.get(leader=request.user)
    target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
    if request.method == "POST":
        form = TeamDataForm(request.POST, request.FILES, instance=target_team)
        mem1 = TeamMemberForm(request.POST, instance=target_members[0])

        if form.is_valid() and mem1.is_valid():
            tmp = form.save(commit=False)
            form.save()
            t1 = mem1.save(commit=False)
            t1.team = tmp
            t1.player_num = target_members.count()
            t1.save()
            # 回傳並顯示
            error_message = '隊伍儲存成功'
            form = TeamDataForm(instance=target_team)
            target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
            real_member_num = target_members.count()
            return render(request, 'idea/show_team.html', locals())
        else:
            print('!!!! modify_team error !!!')
            if mem1.errors:
                error_message = mem1.errors
            elif form.errors:
                error_message = form.errors
    else:
        form = TeamDataForm(instance=target_team)
        mem1 = TeamMemberForm(instance=target_members[0])

    return render(request, 'idea/add_team.html', locals())


def add_member(request):
    check_team = Team.objects.filter(leader=request.user)
    target_team = Team.objects.get(leader=request.user)
    target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
    if request.method == "POST":
        mem2 = AddTeamMemberForm(request.POST)
        if mem2.is_valid():
            # 回傳並顯示
            t1 = mem2.save(commit=False)
            t1.team = target_members[0].team
            t1.player_num = target_members[0].player_num
            t1.save()

            member_count = target_members.count()
            if member_count < 5:
                error_message = '新增隊員成功,請輸入下一筆隊員資料'
            else:
                error_message = '隊伍成員已滿'
            return redirect('show_team')
        else:
            print('!!!! add_member error !!!')
            error_message = mem2.errors
    else:
        member_count = target_members.count()
        if member_count < 5:
            mem1 = AddTeamMemberForm()
        else:
            error_message = '隊員名額已滿'

    return render(request, 'idea/add_member.html', locals())


def modify_member(request):
    check_team = Team.objects.filter(leader=request.user)
    target_team = Team.objects.get(leader=request.user)
    target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
    if request.method == "POST":
        mem2 = AddTeamMemberForm(request.POST)
        if mem2.is_valid():
            # 回傳並顯示
            t1 = mem2.save(commit=False)
            t1.team = target_members[0].team
            t1.player_num = target_members.count()
            t1.save()
            # error_message = '新增隊員成功'
            # form = TeamDataForm(instance=target_team)
            member_count = target_members.count()
            # print(member_count)
            # print(target_members[0].player_num)
            if member_count < 5:
                error_message = '新增隊員成功,請輸入下一筆隊員資料'
            else:
                return redirect('show_team')
        else:
            print('!!!! error !!!')
            error_message = mem2.errors
    else:
        member_count = target_members.count()
        if member_count < 5:
            mem1 = AddTeamMemberForm()
        else:
            error_message = '隊員名額已滿'

    return render(request, 'idea/add_member.html', locals())


def add_files(request):
    check_team = Team.objects.filter(leader=request.user)
    target_team = Team.objects.get(leader=request.user)
    if request.method == "POST":
        form = TeamFilesForm(request.POST, request.FILES, instance=target_team)
        if form.is_valid():
            form.save()
            # 回傳並顯示
            error_message = '檔案儲存成功'
            files = form
        else:
            print('!!!! add_files error !!!')
            if form.errors:
                error_message = form.errors
    else:
        form = TeamFilesForm(instance=target_team)

    return render(request, 'idea/file_list.html', locals())
