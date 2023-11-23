from django import forms
from .models import Signin, Signup


class SigninForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = '__all__'


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'
