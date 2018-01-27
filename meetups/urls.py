from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='all-meetups'), # my-domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    # A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They're generally used in URLs. ( as in Django docs) A slug field in Django is used to store and generate valid URLs for your dynamically created web pages.
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail') # my-domain.com/meetups/<dynamic-path-segment>
]
