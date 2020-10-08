from django.urls import path, include
from idea.views import index,model_form_upload, file_list

urlpatterns = [
    path('', index, name='idea_home'),
    path('uploads', model_form_upload, name='model_form_upload'),
    path('list_files', file_list, name='file_list'),
]
