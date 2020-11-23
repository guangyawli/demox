from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from accounts.forms import ProfileForm
from .models import UserProfile, OauthProvider
from django.contrib import messages
# import logging
import uuid
from idea.models import Team, TeamMember

# Email
from django.core.mail import EmailMultiAlternatives, get_connection
from accounts.models import MailServer, Emails
from django.template import loader

# OAuth
from django.http import HttpResponseRedirect, HttpResponse
from requests_oauthlib import OAuth2Session


def index(request):
    return render(request, 'index.html', locals())


@login_required
def my_profile(request):
    target_item = UserProfile.objects.get(user=request.user)
    role_status = target_item.role_flag
    if request.method == "GET":
        target_form = ProfileForm(instance=target_item)
    elif request.method == "POST":
        target_form = ProfileForm(request.POST, instance=target_item)
        if target_form.is_valid():
            target_form.save()
            error_message = 'Profile 修改成功'
            messages.add_message(request, messages.SUCCESS, error_message)

    render_content = {
        'target_form': target_form,
        'role_status': role_status
    }
    return render(request, 'accounts/profile.html', render_content)


def sign_in(request):
    client_id = OauthProvider.objects.get(provider_name='openedu').client_id
    redirect_uri = OauthProvider.objects.get(provider_name='openedu').redirect_uri
    authorization_base_url = OauthProvider.objects.get(provider_name='openedu').authorization_base_url
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=['email', 'profile', 'user_id'])
    authorization_url, state = oauth.authorization_url(authorization_base_url)
    #  print(authorization_url)
    # request.session['state']=state
    return HttpResponseRedirect(authorization_url)


# @method_decorator(csrf_exempt)
def UserLoginAPI2(request):
    redirect_uri = OauthProvider.objects.get(provider_name='openedu').redirect_uri
    provider_host = OauthProvider.objects.get(provider_name='openedu').provider_host
    client_id = OauthProvider.objects.get(provider_name='openedu').client_id
    client_secret = OauthProvider.objects.get(provider_name='openedu').client_secret
    token_url = OauthProvider.objects.get(provider_name='openedu').token_url
    requestapi = OauthProvider.objects.get(provider_name='openedu').requestapi

    redirect_response = provider_host+request.get_full_path()
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=['email', 'profile', 'user_id'])
    request.session['token'] = oauth.fetch_token(token_url, authorization_response=redirect_response,
                                                 client_secret=client_secret)
    # token2 = oauth.access_token
    # return HttpResponse(token2)
    r = oauth.get(requestapi)

    if User.objects.filter(username=eval(r.text)["username"]).exists():
        user = auth.authenticate(username=eval(r.text)['username'], password=eval(r.text)['id'])
        if user:
            auth.login(request, user)
        return HttpResponseRedirect(provider_host)
    elif r.status_code == 200:
        user = User.objects.create(username=eval(r.text)['username'], email=eval(r.text)["email"])
        user.set_password(eval(r.text)["id"])
        user.save()
        UserProfile.objects.create(user=user)
        auth.login(request, user)
        return HttpResponseRedirect(provider_host)
    else:
        messages.add_message(request, messages.ERROR, '帳號不存在，請重新登入')
        return redirect('home')


# def sign_up(request):
#     if request.user.is_authenticated:
#         return redirect('account_home')
#     else:
#         form = RegisterForm()
#         if request.method == "POST":
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password1']
#                 email = form.cleaned_data['email']
#                 user = User.objects.create(username=username, password=password, email=email, is_active=False)
#                 user.set_password(password)
#                 user.save()
#                 active_key = username
#                 token = '{}'.format(uuid.uuid4().hex[:10])
#                 tprofile, created = UserProfile.objects.get_or_create(user=user, check_code=token)
#                 if created:
#                     tprofile.save()
#                 else:
#                     err_msg = '該帳號已有啟用碼'
#                     messages.add_message(request, messages.ERROR, err_msg)
#                     return redirect('home')
#
#                 tmp_server = MailServer.objects.get(id=1)
#
#                 conn = get_connection()
#                 conn.username = tmp_server.m_user  # username
#                 conn.password = tmp_server.m_password  # password
#                 conn.host = tmp_server.m_server  # mail server
#                 conn.open()
#
#                 target_mails = []
#                 # target_mails.append('gyli@mail.fcu.edu.tw')
#                 target_mails.append(email)
#                 # print(target_mails)
#                 # print(courses.course_id)
#                 # logging.debug(str(target_mails) + str(datetime.now()))
#
#                 test_from = Emails.objects.get(e_status='register_confirm').e_from
#                 test_title = Emails.objects.get(e_status='register_confirm').e_title
#                 # announcement = Emails.objects.get(e_status='default').e_content
#                 context = {
#                     'coding101_url': request.get_host,
#                     'check_token': token,
#                     'active_key': active_key
#                 }
#                 # print(courses.course_name)
#                 email_template_name = 'accounts/mail_register.html'
#                 t = loader.get_template(email_template_name)
#
#                 mail_list = target_mails
#
#                 subject, from_email, to = test_title, test_from, mail_list
#                 html_content = t.render(dict(context))  # str(test_content)
#                 # msg = EmailMultiAlternatives(subject, html_content, from_email, bcc=to)
#                 msg = EmailMultiAlternatives(subject, html_content, from_email, to=to)
#                 msg.attach_alternative(html_content, "text/html")
#                 # msg.attach_file(STATIC_ROOT + 'insights_readme.pdf')
#                 conn.send_messages([msg, ])  # send_messages发送邮件
#
#                 conn.close()
#
#                 err_msg = '請至註冊信箱：' + email + ' 收信並點選信中連結啟用帳號'
#                 messages.add_message(request, messages.SUCCESS, err_msg)
#                 return redirect('home')
#             else:
#                 err_msg = [(k, v[0]) for k, v in form.errors.items()]
#                 for i in range(len(err_msg)):
#                     messages.add_message(request, messages.ERROR, err_msg[i][1])
#                 # messages.get_messages(request)
#                 # return redirect('Register')
#
#         return render(request, 'accounts/register.html', locals())
#
#
# def sign_in(request):
#     if request.user.is_authenticated:
#         return redirect('account_home')
#     else:
#         form = LoginForm()
#         if request.method == "POST":
#             username = request.POST.get("username")
#             password = request.POST.get("password")
#
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 if request.user.is_active:
#                     messages.add_message(request, messages.SUCCESS, '登入成功')
#                     return redirect('account_home')
#                 # else:
#                 #     logout(request, user)
#                 #     messages.add_message(request, messages.INFO, '請前往註冊信箱，並點擊註冊信連結啟用帳號')
#                 #     messages.add_message(request, messages.WARNING, '或填寫帳號資料重送認證信')
#                 #     return redirect('resend_active_letter')
#             else:
#                 try:
#                     tmpuser = User.objects.get(username=username)
#                     if tmpuser.is_active:
#                         messages.add_message(request, messages.ERROR, '密碼錯誤')
#                     else:
#                         messages.add_message(request, messages.ERROR, '帳號未啟用，請至註冊信箱收取認證信')
#                     return redirect('Login')
#                 except User.DoesNotExist:
#                     messages.add_message(request, messages.ERROR, '無此帳號')
#                     return redirect('Login')
#
#         return render(request, 'accounts/login.html', locals())


def log_out(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, '登出成功')
    return redirect('home')


# def activate_user(request, active_key, token):
#     # logging.basicConfig(filename=os.path.join("log_files", 'mail_log'), level=logging.DEBUG)
#     try:
#         user = User.objects.get(username=active_key, userprofile__check_code=token)
#     except User.DoesNotExist:
#         messages.add_message(request, messages.ERROR, '該帳號不存在，請重新登入')
#         return redirect('Login')
#     if user.is_active:
#         messages.add_message(request, messages.SUCCESS, '帳號已啟用')
#         return redirect('Login')
#     else:
#         user.is_active = True
#         user.save()
#         messages.add_message(request, messages.SUCCESS, '啟用成功')
#         return redirect('Login')
#
#
# def request_reset(request):
#     rform = ResetRequestForm()
#     if request.method == "POST":
#         try:
#             user = User.objects.get(username=request.POST['username'])
#             active_key = user.username
#             token = '{}'.format(uuid.uuid4().hex[:10])
#             if user.is_active:
#                 tprofile = UserProfile.objects.get(user=user)
#                 tprofile.check_code = token
#                 tprofile.save()
#                 tmp_server = MailServer.objects.get(id=1)
#                 conn = get_connection()
#                 conn.username = tmp_server.m_user  # username
#                 conn.password = tmp_server.m_password  # password
#                 conn.host = tmp_server.m_server  # mail server
#                 conn.open()
#
#                 target_mails = []
#                 # target_mails.append('gyli@mail.fcu.edu.tw')
#                 target_mails.append(user.email)
#                 # print(target_mails)
#                 # print(courses.course_id)
#                 # logging.debug(str(target_mails) + str(datetime.now()))
#
#                 test_from = Emails.objects.get(e_status='password_reset').e_from
#                 test_title = Emails.objects.get(e_status='password_reset').e_title
#                 # announcement = Emails.objects.get(e_status='default').e_content
#                 context = {
#                     'coding101_url': request.get_host,
#                     'check_token': token,
#                     'active_key': active_key
#                 }
#                 # print(courses.course_name)
#                 email_template_name = 'accounts/mail_reset_pwd.html'
#                 t = loader.get_template(email_template_name)
#
#                 mail_list = target_mails
#
#                 subject, from_email, to = test_title, test_from, mail_list
#                 html_content = t.render(dict(context))  # str(test_content)
#                 # msg = EmailMultiAlternatives(subject, html_content, from_email, bcc=to)
#                 msg = EmailMultiAlternatives(subject, html_content, from_email, to=to)
#                 msg.attach_alternative(html_content, "text/html")
#                 # msg.attach_file(STATIC_ROOT + 'insights_readme.pdf')
#                 conn.send_messages([msg, ])  # send_messages发送邮件
#
#                 conn.close()
#                 messages.add_message(request, messages.INFO, '請前往註冊信箱收取重置連結')
#             else:
#                 messages.add_message(request, messages.INFO, '請先至註冊信箱啟用該帳號')
#         except User.DoesNotExist:
#             messages.add_message(request, messages.ERROR, '該帳號不存在')
#
#         return redirect('request_reset')
#
#     context = {
#         'target': "要求重置密碼",
#         'rform': rform
#     }
#
#     return render(request, 'accounts/reset_request.html', context)
#
#
# def reset_user(request, active_key, token):
#     # logging.basicConfig(filename=os.path.join("log_files", 'mail_log'), level=logging.DEBUG)
#     try:
#         user = User.objects.get(username=active_key, userprofile__check_code=token)
#         rform = ResetPwdForm(request.POST, instance=user)
#         if request.method == "POST":
#             if rform.is_valid():
#                 password = rform.cleaned_data['password1']
#                 user.set_password(password)
#                 user.save()
#                 err_msg = '密碼重置成功'
#                 messages.add_message(request, messages.SUCCESS, err_msg)
#                 return redirect('Login')
#             else:
#                 err_msg = [(k, v[0]) for k, v in rform.errors.items()]
#                 for i in range(len(err_msg)):
#                     messages.add_message(request, messages.ERROR, err_msg[i][1])
#
#                 return redirect("reset_user", active_key=active_key, token=token)
#         else:
#             context = {
#                 'target': "重置密碼",
#                 'rform': rform
#             }
#             return render(request, 'accounts/enter_reset.html', context)
#     except User.DoesNotExist:
#         messages.add_message(request, messages.ERROR, '該帳號不存在')
#         return redirect('request_reset')
#
#
# def resend_active_letter(request):
#     if request.method == "POST":
#         try:
#             user = User.objects.get(username=request.POST['username'])
#             active_key = user.username
#             if user.is_active:
#                 messages.add_message(request, messages.ERROR, '該帳號已啟用')
#             else:
#                 token = '{}'.format(uuid.uuid4().hex[:10])
#                 tprofile, created = UserProfile.objects.get_or_create(user=user)
#                 tprofile.check_code = token
#                 tprofile.save()
#
#                 tmp_server = MailServer.objects.get(id=1)
#
#                 conn = get_connection()
#                 conn.username = tmp_server.m_user  # username
#                 conn.password = tmp_server.m_password  # password
#                 conn.host = tmp_server.m_server  # mail server
#                 conn.open()
#
#                 target_mails = []
#                 # target_mails.append('gyli@mail.fcu.edu.tw')
#                 target_mails.append(user.email)
#                 # print(target_mails)
#                 # print(courses.course_id)
#                 # logging.debug(str(target_mails) + str(datetime.now()))
#
#                 test_from = Emails.objects.get(e_status='register_confirm').e_from
#                 test_title = Emails.objects.get(e_status='register_confirm').e_title
#                 # announcement = Emails.objects.get(e_status='default').e_content
#                 context = {
#                     'coding101_url': request.get_host,
#                     'check_token': token,
#                     'active_key': active_key
#                 }
#                 # print(courses.course_name)
#                 email_template_name = 'accounts/mail_register.html'
#                 t = loader.get_template(email_template_name)
#
#                 mail_list = target_mails
#
#                 subject, from_email, to = test_title, test_from, mail_list
#                 html_content = t.render(dict(context))  # str(test_content)
#                 # msg = EmailMultiAlternatives(subject, html_content, from_email, bcc=to)
#                 msg = EmailMultiAlternatives(subject, html_content, from_email, to=to)
#                 msg.attach_alternative(html_content, "text/html")
#                 # msg.attach_file(STATIC_ROOT + 'insights_readme.pdf')
#                 conn.send_messages([msg, ])  # send_messages发送邮件
#
#                 conn.close()
#
#                 err_msg = '請至註冊信箱：' + user.email + ' 收信並點選信中連結啟用帳號'
#                 messages.add_message(request, messages.SUCCESS, err_msg)
#                 return redirect('home')
#         except User.DoesNotExist:
#             messages.add_message(request, messages.ERROR, '該帳號不存在')
#
#             return redirect('resend_active_letter')
#     else:
#         rform = ResendConfirmForm()
#         context = {
#             'target': "重寄認證信",
#             'rform': rform
#         }
#         return render(request, 'accounts/reset_request.html', context)
