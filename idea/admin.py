from django.contrib import admin

# Register your models here.
from .models import Team, MemberTemp, TeamMember, TeamScore


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_topic', 'team_school', 'team_teacher', 'leader', 'readme', 'affidavit',
                    'video_link', 'code_link')
    list_filter = ("team_name", "team_school")
    search_fields = ("team_name", "team_teacher")
    ordering = ("team_name",)


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('team', 'member_name', 'school_name', 'department_name', 'department_grade', 'phone_number',
                    'email_addr')
    list_filter = ("member_name", "department_name")
    ordering = ("member_name",)


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)

admin.site.register(MemberTemp)
admin.site.register(TeamScore)
