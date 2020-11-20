from django.contrib import admin
from accounts.models import MailServer, Emails, UserProfile, OauthProvider

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_code')


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('e_from', 'e_title', 'e_content', 'e_status')


class MailServerAdmin(admin.ModelAdmin):
    list_display = ('m_server', 'm_user', 'm_password')


class OauthProviderAdmin(admin.ModelAdmin):
    list_display = ('provider_name', 'provider_host')


admin.site.register(Emails, EmailsAdmin)
admin.site.register(MailServer, MailServerAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(OauthProvider, OauthProviderAdmin)