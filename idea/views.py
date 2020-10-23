from django.shortcuts import render, redirect

from .forms import TeamDataForm, TeamMember, TeamMemberForm, AddTeamMemberForm, TeamFilesForm
from .models import Team
# from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'idea/index.html', locals())


def file_list(request):
    check_team = Team.objects.filter(leader=request.user).exists()
    if check_team:
        target_team = Team.objects.get(leader=request.user)
        if target_team.readme or target_team.video_link or target_team.affidavit:
            files = target_team
            if files.video_link != '':
                video_id = files.video_link.split('?v=')[1]
                video_embed_link = 'https://www.youtube.com/embed/' + video_id
            else:
                video_embed_link = ''
        else:
            return redirect('add_files')
    else:
        return redirect('add_team')

    return render(request, 'idea/file_list.html', {'files': files,'video_embed_link':video_embed_link})


def show_team(request):
    check_team = Team.objects.filter(leader=request.user)
    if check_team.exists():
        if request.method == "GET":
            target_team = Team.objects.get(leader=request.user)
            target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
            form = target_team
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
            return redirect('show_team')
            # form = TeamDataForm(instance=target_team)
            # real_member_num = target_members.count()
            # return render(request, 'idea/show_team.html', locals())
        else:
            print('!!!! error add_team !!!')
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
            return redirect('show_team')
            # form = TeamDataForm(instance=target_team)
            # target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
            # real_member_num = target_members.count()
            # return render(request, 'idea/show_team.html', locals())
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
    target_title = '新增'
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
    target_title = '修改'
    check_team = Team.objects.filter(leader=request.user)
    target_team = Team.objects.get(leader=request.user)
    target_members = TeamMember.objects.filter(team__team_name=target_team.team_name)
    if request.POST.get('btn_target_name'):
        modify_target = TeamMember.objects.get(id=request.POST.get('btn_target_name'),
                                               team__team_name=target_team.team_name)
        target_id = modify_target.id
        mem1 = AddTeamMemberForm(instance=modify_target)
    else:
        if request.method == "POST":
            save_target = TeamMember.objects.get(id=request.POST['target_id'],
                                                 team__team_name=target_team.team_name)
            mem2 = AddTeamMemberForm(request.POST, instance=save_target)
            if mem2.is_valid():
                # 回傳並顯示
                t1 = mem2.save(commit=False)
                t1.team = target_members[0].team
                t1.player_num = target_members.count()
                t1.save()
                return redirect('show_team')
            else:
                print('!!!! modify_member error !!!')
                error_message = mem2.errors

    return render(request, 'idea/add_member.html', locals())


def del_member(request):
    check_team = Team.objects.filter(leader=request.user)
    target_team = Team.objects.get(leader=request.user)
    target_mem = TeamMember.objects.get(team__team_name=target_team.team_name, id=request.POST.get('btn_target_name'))
    if check_team and target_mem:
        target_mem.delete()
        return redirect('show_team')
    else:
        error_message = '隊伍刪除失敗'
        error_link = 'show_team'
        return render(request, 'idea/show_team.html', locals())


def add_files(request):
    check_team = Team.objects.filter(leader=request.user)
    if not check_team.exists():
        return redirect('add_team')
    else:
        target_team = check_team.get()
        if request.method == "POST":
            post_form = TeamFilesForm(request.POST, request.FILES, instance=target_team)
            if post_form.is_valid():
                post_form.save()
                return redirect('file_list')
                # 回傳並顯示
                # error_message = '檔案儲存成功'
                # check_team = Team.objects.filter(leader=request.user).exists()
                # if check_team:
                #     target_team = Team.objects.get(leader=request.user)
                #     if target_team.readme or target_team.video_link or target_team.affidavit:
                #         files = target_team
                #     else:
                #         files = None
                # else:
                #     files = None
                # return render(request, 'idea/file_list.html', {'files': files})
            else:
                print('!!!! add_files error !!!')
                if post_form.errors:
                    error_message = post_form.errors
        else:
            post_form = TeamFilesForm(instance=target_team, initial={})

        return render(request, 'idea/file_list.html', locals())

