from django import forms
from .views import UserCustom

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserCustom
        fields = ['username','email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

