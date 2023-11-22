from django.shortcuts import render
from .forms import SigninForm

# Create your views here.
def sign_in(request):
    form = SigninForm()
    context = {'form': form}
    return render(request,'sign-in.html')