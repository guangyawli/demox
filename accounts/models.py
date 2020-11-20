from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
    check_code = models.CharField(max_length=10, blank=True, verbose_name='檢查碼')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='帳號名稱')

    def __str__(self):
        return self.user.username


class Emails(models.Model):
    e_from = models.CharField(max_length=50, blank=False, verbose_name='寄件者', default='推動大學程式設計教學 <admin@coding101.tw>')
    e_title = models.CharField(max_length=100, blank=False, verbose_name='信件標題', default='default_title')
    e_content = RichTextField(blank=True, verbose_name='信件內容', null=True)
    e_status = models.CharField(max_length=50, verbose_name='功能', blank=True)

    def __str__(self):
        return self.e_title


class MailServer(models.Model):
    m_server = models.CharField(max_length=50, blank=False, verbose_name='MAIL伺服器', default='mail.gandi.net')
    m_user = models.CharField(max_length=50, blank=False, verbose_name='帳號', default='admin@coding101.tw')
    m_password = models.CharField(max_length=30, blank=False, verbose_name='密碼', default='default_password')

    def __str__(self):
        return self.m_server


class OauthProvider(models.Model):
    provider_name = models.CharField(max_length=30, verbose_name='Provider名稱', default='openedu')
    provider_host = models.CharField(max_length=40, verbose_name='host網址', default='https://courses-api.openedu.tw')
    client_id = models.CharField(max_length=80, verbose_name='Client ID')
    client_secret = models.CharField(max_length=150, verbose_name='Client Secret')
    requestapi = models.CharField(max_length=70, verbose_name='api網址',
                                  default='https://courses-api.openedu.tw/oauth2/user_info')
    authorization_base_url = models.CharField(max_length=70, verbose_name='auth網址',
                                              default='https://courses-api.openedu.tw/oauth2/authorize')
    token_url = models.CharField(max_length=70, verbose_name='token網址',
                                 default='https://courses-api.openedu.tw/oauth2/access_token')
    redirect_uri = models.CharField(max_length=70, verbose_name='return網址',
                                    default='http://demox.twshop.asia/accounts/rlogin')

    def __str__(self):
        return self.provider_name
