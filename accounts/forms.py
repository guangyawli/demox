from django import forms
from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['check_code', 'user', 'role_flag', 'master_url', 'master_email', 'master_status']
        widgets = {
            'real_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫真實姓名',
                                                'id': 'id_real_name'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫任職/就讀學校',
                                             'id': 'id_school'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫任職/就讀科系',
                                                 'id': 'id_department'})
        }


class ApplyMasterForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['check_code', 'user', 'role_flag', 'master_status']
        widgets = {
            'real_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫真實姓名',
                                                'id': 'id_real_name'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫任職學校',
                                             'id': 'id_school'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫任職科系',
                                                 'id': 'id_department'}),
            'master_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '填寫任職學校個人主頁（含Email）',
                                                 'id': 'id_master_url'}),
            'master_email': forms.EmailInput(attrs={'class': 'form-control',
                                                    'placeholder': '填寫任職學校Email(例如：xxx.edu.tw)',
                                                    'id': 'id_master_email'})
        }


# class RegisterForm(UserCreationForm):
#     username = forms.CharField(
#         label="帳號",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     email = forms.EmailField(
#         label="電子郵件",
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )
#     password1 = forms.CharField(
#         label="密碼",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#     password2 = forms.CharField(
#         label="密碼確認",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#     def clean_email(self):
#         user_name = self.cleaned_data['username']
#         email = self.cleaned_data['email']
#         obj = User.objects.filter(email=email).exclude(username=user_name)
#         if obj:
#             raise forms.ValidationError('此信箱已註冊')
#         else:
#             return email


# class ResetRequestForm(forms.Form):
#     username = forms.CharField(
#         label="重置帳號",
#         widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'reset_account'})
#     )
#
#
# class ResetPwdForm(UserCreationForm):
#     password1 = forms.CharField(
#         label="輸入新密碼",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#     password2 = forms.CharField(
#         label="密碼確認",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#
#     class Meta:
#         model = User
#         fields = ('password1', 'password2')
#         exclude = ('username', 'email',)
#
#
# class ResendConfirmForm(forms.Form):
#     username = forms.CharField(
#         label="請輸入帳號",
#         widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'resend_confirm'})
#     )
