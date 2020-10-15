from django.urls import path, include
from idea.views import index, team_data_modify, file_list


urlpatterns = [
    path('', index, name='idea_home'),
    path('modify_team_data', team_data_modify, name='team_data_modify'),
    path('list_files', file_list, name='file_list'),
]
