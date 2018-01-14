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


