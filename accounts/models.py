from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True)
    team_title = models.CharField(max_length=50)
    team_school = models.CharField(max_length=50)
    team_teacher = models.CharField(max_length=50)
    leader_name = models.CharField(max_length=50, blank=False)


class TeamMember(models.Model):
    team_name = models.OneToOneField(Team)
    member_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=60)
    department_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)




