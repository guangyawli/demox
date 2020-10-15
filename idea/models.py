from datetime import datetime
import os
import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# def user_readme_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
#     return os.path.join("readme_files", filename)

def user_readme_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
    today = datetime.now()
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(instance.team_name, today, ext)
    return os.path.join("readme_files", filename)


class Team(models.Model):
    team_name = models.CharField(max_length=40, unique=True)
    team_topic = models.CharField(max_length=50)
    team_school = models.CharField(max_length=40)
    team_teacher = models.CharField(max_length=30)
    leader = models.OneToOneField(User, on_delete=models.CASCADE)
    video_link = models.URLField(blank=True)
    code_link = models.URLField(blank=True)
    readme = models.FileField(upload_to=user_readme_path, blank=True)


class TeamMember(models.Model):
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=30)
    school_name = models.CharField(max_length=50)
    department_name = models.CharField(max_length=30)
    department_grade = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email_addr = models.EmailField()


class TeamScore(models.Model):
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    score1 = models.FloatField(default=0)
    score2 = models.FloatField(default=0)
    score3 = models.FloatField(default=0)
    judge_user = models.FloatField(default=0)
    total_score = models.FloatField(default=0)


class MemberTemp(models.Model):
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_num = models.CharField(max_length=10, choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
                                  default='1')
    member_name1 = models.CharField(max_length=30)
    school_name1 = models.CharField(max_length=50)
    department_name1 = models.CharField(max_length=30)
    department_grade1 = models.CharField(max_length=10)
    phone_number1 = models.CharField(max_length=20)
    email_addr1 = models.EmailField(blank=True)
    member_name2 = models.CharField(max_length=30, blank=True)
    school_name2 = models.CharField(max_length=50, blank=True)
    department_name2 = models.CharField(max_length=30, blank=True)
    department_grade2 = models.CharField(max_length=10, blank=True)
    phone_number2 = models.CharField(max_length=20, blank=True)
    email_addr2 = models.EmailField(blank=True)
    member_name3 = models.CharField(max_length=30, blank=True)
    school_name3 = models.CharField(max_length=50, blank=True)
    department_name3 = models.CharField(max_length=30, blank=True)
    department_grade3 = models.CharField(max_length=10, blank=True)
    phone_number3 = models.CharField(max_length=20, blank=True)
    email_addr3 = models.EmailField(blank=True)
    member_name4 = models.CharField(max_length=30, blank=True)
    school_name4 = models.CharField(max_length=50, blank=True)
    department_name4 = models.CharField(max_length=30, blank=True)
    department_grade4 = models.CharField(max_length=10, blank=True)
    phone_number4 = models.CharField(max_length=20, blank=True)
    email_addr4 = models.EmailField(blank=True)
    member_name5 = models.CharField(max_length=30, blank=True)
    school_name5 = models.CharField(max_length=50, blank=True)
    department_name5 = models.CharField(max_length=30, blank=True)
    department_grade5 = models.CharField(max_length=10, blank=True)
    phone_number5 = models.CharField(max_length=20, blank=True)
    email_addr5 = models.EmailField(blank=True)
