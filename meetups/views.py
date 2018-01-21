from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.
def index(request):
    # return HttpResponse("Hello World!")

    # Slug - Slug is unique identifier that has a URL friendly format and a serach engine optimized format (i.e., Human readable format instead of cryptic combination of characters).
    # meetups = [
    #     {
    #         'title': 'A First Meetup', 
    #         'location': 'Bengaluru', 
    #         'slug': 'a-first-meetup'
    #     },
    #     {
    #         'title': 'A Second Meetup', 
    #         'location': 'Paris', 
    #         'slug': 'a-second-meetup'
    #     },
    #     {
    #         'title': 'A Third Meetup', 
    #         'location': 'Berlin', 
    #         'slug': 'a-third-meetup'
    #     }
    # ]

    meetups = Meetup.objects.all()

    # Django's template engine provides a powerful mini-language for defining the user-facing layer of your application, encouraging a clean separation of application and presentation logic. Templates can be maintained by anyone with an understanding of HTML; no knowledge of Python is required.
    # Django Template Engine renders or interpolates below HTML file using the python dictionary. Final HTML file is sent to client machine.
    return render(request, 'meetups/index.html', {
        # 'show_meetups': True,
        'meetups': meetups
    })


