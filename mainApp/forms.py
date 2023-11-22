from django import forms
from .models import Signin, Signup

class SigninForm(forms.ModelForm):

    class Meta:
        fields = ['__all__']
        model = Signin

class SignupForm(forms.ModelForm):

    class Meta:
        fields = ['__all__']
        model = Signup
