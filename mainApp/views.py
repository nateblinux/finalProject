import traceback
from encodings import undefined

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SigninForm, SignupForm
import requests
import datetime
import json
from .models import *


def ticket_master(request):  # APIrequest
    if not request.POST:
        return render(request, 'ticketmaster_base.html')

    if not request.POST.get('genre'):
        context = {
            'error': "input",
            'message': "please enter an event type"
        }

    if not request.POST.get('city'):
        context = {
            'error': "input",
            'message': "please enter a city"
        }
        return render(request, 'ticketmaster_results.html', context=context)

    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    parameters = {
        "size": "20",
        "apikey": "W8KLJ3KiVgrPoXNNAbenReqGAuhGnZ1i",
        "sort": "date,asc",
        "classificationName": request.POST.get('genre'),
        "city": request.POST.get('city'),
    }

    events_list = []
    response = requests.get(url, params=parameters)
    data = response.json()
    num_of_results = data["page"]["totalElements"]

    if data["page"]["totalElements"] == 0:
        context = {
            'events': events_list,
            'num_of_results': data["page"]["totalElements"],
            'error': "no results found"
        }
        return render(request, 'ticketmaster_results.html', context=context)

    if num_of_results > 20:
        num_of_results = 20

    data = data['_embedded']
    events = data['events']

    for event in events:
        try:
            name = event['name']
            images = event['images']
            image_url = images[0]['url']
            highest_res = images[0]['width']
            lowest_res = images[0]['width']
            low_res_img = ""

            # get highest size here
            for image in images:
                if image['ratio'] == "16_9" and image['width'] > highest_res:
                    image_url = image['url']
                    highest_res = image['width']

            try:
                start_date = event['dates']['start']['dateTime']
                date_time = datetime.datetime.fromisoformat(start_date)
                formatted_date = date_time.strftime("%a %b %d %Y")
                formatted_time = date_time.strftime("%I:%M %p")
            except:
                formatted_time = ""
                formatted_date = "N/A"

            spotify_link = ''
            facebook_link = ''
            twitter_link = ''

            embedded = event['_embedded']
            try:
                attractions = embedded['attractions']
                if attractions[0]['externalLinks']:
                    external_links = embedded['attractions'][0][
                        'externalLinks']  # problem around here getting spotify URL
                    if external_links['spotify']:
                        spotify_link = external_links['spotify'][0]['url']
                    if external_links['facebook']:
                        facebook_link = external_links['facebook'][0]['url']
                    if external_links['twitter']:
                        twitter_link = external_links['twitter'][0]['url']
            except:
                print('not there')

            venue = embedded['venues'][0]
            venue_name = venue['name']
            venue_city = venue['city']['name']
            venue_state = venue['state']['name']
            venue_address = venue['address']['line1']
            ticket_link = event['url']
            print(ticket_link)
            event_details = {
                'venue_name': venue_name,
                'venue_city': venue_city,
                'venue_state': venue_state,
                'venue_address': venue_address,
                'ticket_link': ticket_link,
                'twitter_link': twitter_link,
                'facebook_link': facebook_link,
                'spotify_link': spotify_link,
                'formatted_time': formatted_time,
                'formatted_date': formatted_date,
                'image_url': image_url,
                'name': name,
            }
            events_list.append(event_details)
        except Exception as e:
            print(event)
            print(traceback.format_exc())

    context = {
        'events': events_list,
        'num_of_results': num_of_results,
    }

    return render(request, 'ticketmaster_results.html', context=context)


# use this in case you want to have custom fields in User Registration Form
# from django.contrib import messages


# # @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# # if so, index page is rendered. If not, the user is redirected to the login page via login_url
# @login_required(login_url='login')
def home(request):
    # Render the index page
    return render(request, 'authentication/index.html')


def signin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')
        return redirect('signin')
    return render(request, 'authentication/sign-in.html')


def signup(request):

    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')

    return render(request, 'authentication/sign-up.html')


def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

