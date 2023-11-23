from django.shortcuts import render
from .forms import SigninForm, SignupForm


# Create your views here.
def sign_in(request):
    form = SigninForm()
    context = {'form': form}
    return render(request, 'sign-in.html', context)


def sign_up(request):
    form = SignupForm()
    context = {'form': form}
    return render(request, 'sign-up.html', context)


def ticket_master(request):
    return render(request, 'ticketmaster.html')
