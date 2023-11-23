from django.shortcuts import render, redirect
from .forms import SigninForm, SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# We won't be needing these definitions below
def sign_in(request):
    form = SigninForm()
    context = {'form': form}
    return render(request, 'sign-in.html', context)


def sign_up(request):
    form = SignupForm()
    context = {'form': form}
    return render(request, 'sign-up.html', context)

# Except this one
def ticket_master(request):
    return render(request, 'ticketmaster.html')
