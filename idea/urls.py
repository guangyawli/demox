from django.urls import path, include
from idea.views import index, file_list, show_team, add_team, add_member, modify_team, modify_member, add_files


urlpatterns = [
    path('', index, name='idea_home'),
    # path('modify_team_data', team_data_modify, name='team_data_modify'),
    path('list_files', file_list, name='file_list'),
    path('files_add', add_files, name='add_files'),
    path('team_show', show_team, name='show_team'),
    path('team_add', add_team, name='add_team'),
    path('team_modify', modify_team, name='modify_team'),
    path('member_add', add_member, name='add_member'),
    path('member_modify', modify_member, name='modify_member'),
]
