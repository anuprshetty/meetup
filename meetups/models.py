from django.db import models

# Create your models here.

# ORM (Object-Relational Mapper)
# - An object-relational mapper is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.
# - Object–Relational Mapping in computer science is a programming technique for converting data between incompatible type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# Django automatically creates a database table for each model.
# Later we can store the instances of the model in that database table.
class Meetup(models.Model):
    title = models.CharField(max_length=200) # CharField() for shorter text.
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True) # unique=True --> Django also creates an index behind the scenes for slug to make querying for slugs more efficient.
    description = models.TextField() # TextField() for longer text.
    # models.ImageField() is dependent on Pillow python package.
    image = models.ImageField(upload_to='images') # Pointer or reference to the image file is stored in the image field of Meetup table in DB.
    # One-To-Many Relationship 
    #   - A location can have multiple meetups.
    #   (OR)
    #   - Multiple meetups can have single location.
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # Many-To-Many Relationship
    #   - A meetup can have multiple participants (AND) A participant can sign up for multiple meetups.
    participants = models.ManyToManyField(Participant, blank=True)

    # Overwriting __str__() method.
    def __str__(self):
        # Returning a formatted string.
        return f'{self.title} - {self.slug}'
