from datetime import datetime
import os
import uuid

from django.core import validators
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# def user_readme_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
#     return os.path.join("readme_files", filename)
#
# def user_readme_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
#     today = datetime.now()
#     ext = filename.split('.')[-1]
#     filename = '{}{}.{}'.format(instance.team_name, today, ext)
#     return os.path.join("readme_files", filename)
#
#
# def user_affidavit_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
#     today = datetime.now()
#     ext = filename.split('.')[-1]
#     filename = '{}{}.{}'.format(instance.team_name, today, ext)
#     return os.path.join("affidavit_files", filename)
#
#
# class Team(models.Model):
#     team_name = models.CharField(max_length=40, unique=True)
#     team_topic = models.CharField(max_length=50)
#     team_school = models.CharField(max_length=40)
#     team_teacher = models.CharField(max_length=30)
#     leader = models.OneToOneField(User, on_delete=models.CASCADE)
#     video_link = models.URLField(blank=True)
#     code_link = models.URLField(blank=True)
#     readme = models.FileField(upload_to=user_readme_path, blank=True,
#                               validators=[validators.FileExtensionValidator(['pdf'], message='必須為pdf格式')])
#     affidavit = models.FileField(upload_to=user_affidavit_path, blank=True,
#                                  validators=[validators.FileExtensionValidator(['pdf'], message='必須為pdf格式')])
#
#     def __str__(self):
#         return self.team_name
#
#
# class TeamMember(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     member_name = models.CharField(max_length=30)
#     school_name = models.CharField(max_length=50)
#     department_name = models.CharField(max_length=30)
#     department_grade = models.IntegerField(default=1)
#     phone_number = models.CharField(max_length=20)
#     email_addr = models.EmailField()
#     player_num = models.IntegerField(default=1)
#     # player_num = models.CharField(max_length=10, choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
#     #                               default='1')
#
#     def __str__(self):
#         return self.team.team_name



