from django.urls import path, include
from idea.views import index


urlpatterns = [
    path('', index, name='idea_home'),
]
