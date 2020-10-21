from django import forms
from .models import Team, TeamMember


class TeamDataForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'team_topic', 'team_school', 'team_teacher', 'leader', 'video_link', 'readme',
                  'affidavit')
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'team_topic': forms.TextInput(attrs={'class': 'form-control'}),
            'team_school': forms.TextInput(attrs={'class': 'form-control'}),
            'team_teacher': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'leader': forms.HiddenInput(attrs={'class': 'form-control'}),
            'video_link': forms.URLInput(attrs={'class': 'form-control'}),
            'readme': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'affidavit': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_readme(self):
        if self.cleaned_data['readme']:
            file = self.cleaned_data['readme']
            ext = file.name.split('.')[-1].lower()
            if ext not in ["pdf"]:
                raise forms.ValidationError("Only pdf files are allowed.")
            # return cleaned data is very important.
            return file

    def clean_affidavit(self):
        if self.cleaned_data['affidavit']:
            file = self.cleaned_data['affidavit']
            ext = file.name.split('.')[-1].lower()
            if ext not in ["pdf"]:
                raise forms.ValidationError("Only pdf files are allowed.")
            # return cleaned data is very important.
            return file


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        exclude = ['team']
        widgets = {
            'member_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'department_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'department_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'player_num': forms.NumberInput(attrs={'class': 'form-control', 'id': "player_num"}),
        }

    def clean_department_grade(self):
        if self.cleaned_data['department_grade']:
            target = self.cleaned_data['department_grade']
            if target not in range(1, 10):
                raise forms.ValidationError(" 請填寫 1~9 數字 ")
            return target


class AddTeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        exclude = ['team', 'player_num']
        widgets = {
            'member_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'department_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'department_grade': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email_addr': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
        }


class TeamFilesForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ['team_topic', 'team_school', 'team_teacher', 'leader']
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'video_link': forms.URLInput(attrs={'class': 'form-control', 'required': 'required'}),
            'readme': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': 'required'}),
            'affidavit': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

    def clean_readme(self):
        if self.cleaned_data['readme']:
            file = self.cleaned_data['readme']
            ext = file.name.split('.')[-1].lower()
            if ext not in ["pdf"]:
                raise forms.ValidationError("Only pdf files are allowed.")
            # return cleaned data is very important.
            return file

    def clean_affidavit(self):
        if self.cleaned_data['affidavit']:
            file = self.cleaned_data['affidavit']
            ext = file.name.split('.')[-1].lower()
            if ext not in ["pdf"]:
                raise forms.ValidationError("Only pdf files are allowed.")
            # return cleaned data is very important.
            return file

