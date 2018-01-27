from django.contrib import admin
from .models import Meetup, Location, Participant


# MeetupAdmin class is used to configure Meetup model in admin area/panel.
class MeetupAdmin(admin.ModelAdmin):
    # Displays Meetup model instances with below fields as columns.
    list_display = ('title', 'date', 'location')
    # Adds filter functionality with below fields.
    list_filter = ('location', 'date')
    # Auto generate/populate slug field based on title field.
    prepopulated_fields = {
        'slug': ('title',) # one-element-tuple-notation
        }


# Register your models here.
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
