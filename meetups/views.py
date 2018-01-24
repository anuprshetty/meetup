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


def meetup_details(request, meetup_slug):
    # print(meetup_slug)
    # selected_meetup = {
    #     'title': 'A First Meetup', 
    #     'description': 'This is the first meetup!'
    #     }
    # 
    # return render(request, 'meetups/meetup-details.html', {
    #     'meetup_title': selected_meetup['title'],
    #     'meetup_desciption': selected_meetup['description']
    # })

    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()

        # POST method/request
        else:
            # request object has POST property which contains POST request data (In this case, submitted form data).
            # registration_form contains user input + potential validation errors detected by Django.
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=user_email) # was_created flag tells whether a new participant entry was created or not.
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                # 'meetup_title': selected_meetup.title,
                # 'meetup_desciption': selected_meetup.description,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })


