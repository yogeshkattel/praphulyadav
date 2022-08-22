from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # VALIDATE CAPTCHA AND IF ERROR RETURN ERROR MESSAGE DJANGOSIMPLE CAPATCHA
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        captcha = cleaned_data.get('captcha')
        if not captcha:
            raise forms.ValidationError('INVALID  CAPTCHA')
        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
