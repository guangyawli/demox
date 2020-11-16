from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        user_name = self.cleaned_data['username']
        email = self.cleaned_data['email']
        obj = User.objects.filter(email=email).exclude(username=user_name)
        if obj:
            raise forms.ValidationError('此信箱已註冊')
        else:
            return email


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class ResetRequestForm(forms.Form):
    username = forms.CharField(
        label="重置帳號",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'reset_account'})
    )


class ResetPwdForm(UserCreationForm):
    password1 = forms.CharField(
        label="輸入新密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('password1', 'password2')
        exclude = ('username', 'email',)


class ResendConfirmForm(forms.Form):
    username = forms.CharField(
        label="請輸入帳號",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'resend_confirm'})
    )
