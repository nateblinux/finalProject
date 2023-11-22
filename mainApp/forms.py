from django import forms
from .models import Signin

class SigninForm(forms.ModelForm):

    class Meta:
        fields = ['__all__']
        model = Signin
