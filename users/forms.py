from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        captcha = cleaned_data.get('captcha')
        if not captcha:
            raise forms.ValidationError('INVALID  CAPTCHA')
        return cleaned_data

    # validate if username contains @ and .
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' in username or '.' in username:
            raise forms.ValidationError('Username cannot contain @ or .')
        return username

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# login form with username and email
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username/Email'
        self.fields['password'].label = 'Password'


    

