from django.shortcuts import render, redirect
from .forms import SigninForm, SignupForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
import requests
from .models import *


def ticketmaster_results(request): #APIrequest works just trying to figure out taking variables from the post request
    url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=W8KLJ3KiVgrPoXNNAbenReqGAuhGnZ1i&sort=date,asc"
    # parameters = {
    #     "keyword": genre_input,
    #     "city": city_input,
    # }
    context = {
        'genre': 'wow',
        "city": 'wow',
    }
    # response = requests.get(url, params=parameters)
    # print(response.json())
    # data = response.json()

    # data = data['_embedded']
    # numbof_results = data['page']['totalelements']
    # print(numbof_results)
    return render(request, 'ticketmaster_results.html', context)


# Except this one
def ticket_master(request):
    if request.method == 'POST':
        # genre = request.POST.get('genre')   can be used for later to store things to the data base
        # city = request.POST.get('city')
        # Ticket.objects.create(genre=genre, city=city)

        redirect('ticketmaster-results')
    return render(request, 'ticketmaster.html')


# use this in case you want to have custom fields in User Registration Form
# from django.contrib import messages


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')
def index(request):
    # Render the index page
    return render(request, 'accounts/index.html')


def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        # We use Django's UserCreationForm which is a model created by Django to create a new user.
        # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        # If you want to include email as well, switch to our own custom form called UserRegistrationForm
        form = UserCreationForm(request.POST or None)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            # form.save()
            # if you want to log in the user directly after registration, use the following three lines,
            # which logins the user and redirect to index
            user = form.save()
            login(request, user)
            return redirect('index')
            # if you do want to log in the user directly after registration, comment out the three lines above,
            # redirect the user to login page so that after registration the user can enter the credentials
            # return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    # this function authenticates the user based on username and password
    # AuthenticationForm is a form for logging a user in.
    # if the request method is a post
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # redirect the user to index page
            return redirect('index')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    # This is the method to log out the user
    logout(request)
    # redirect the user to index page after logout
    return redirect('index')


# We won't be needing these definitions below
def sign_in(request):
    form = SigninForm()
    context = {'form': form}
    return render(request, 'sign-in.html', context)


def sign_up(request):
    form = SignupForm()
    context = {'form': form}
    return render(request, 'sign-up.html', context)
