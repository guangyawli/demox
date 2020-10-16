from django import forms
from .models import Team, MemberTemp, TeamMember


class TeamDataForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'team_topic', 'team_school', 'team_teacher', 'leader', 'video_link', 'readme',
                  'affidavit')
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_topic': forms.TextInput(attrs={'class': 'form-control'}),
            'team_school': forms.TextInput(attrs={'class': 'form-control'}),
            'team_teacher': forms.TextInput(attrs={'class': 'form-control'}),
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
        exclude = ['team_name']
        widgets = {
            'member_name': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class MemberTempForm(forms.ModelForm):
    class Meta:
        model = MemberTemp
        exclude = ['team']
        widgets = {
            'player_num': forms.Select(attrs={'class': 'form-control', 'id': "player_num"}),
            'member_name1': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name1': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name1': forms.TextInput(attrs={'class': 'form-control'}),
            'department_grade1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number1': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr1': forms.EmailInput(attrs={'class': 'form-control'}),
            'member_name2': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name2': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name2': forms.TextInput(attrs={'class': 'form-control'}),
            'department_grade2': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number2': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr2': forms.EmailInput(attrs={'class': 'form-control'}),
            'member_name3': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name3': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name3': forms.TextInput(attrs={'class': 'form-control'}),
            'department_grade3': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number3': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr3': forms.EmailInput(attrs={'class': 'form-control'}),
            'member_name4': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name4': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name4': forms.TextInput(attrs={'class': 'form-control'}),
            'department_grade4': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number4': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr4': forms.EmailInput(attrs={'class': 'form-control'}),
            'member_name5': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name5': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name5': forms.TextInput(attrs={'class': 'form-control'}),
            'department_grade5': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number5': forms.TextInput(attrs={'class': 'form-control'}),
            'email_addr5': forms.EmailInput(attrs={'class': 'form-control'})
        }

