from django.contrib import admin

# Register your models here.
from .models import Team, MemberTemp


admin.site.register(Team)
admin.site.register(MemberTemp)