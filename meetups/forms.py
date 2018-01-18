from django import forms
# from .models import Participant


# Django infer a form and the validation rules from a model defined in the application.
# class RegistrationForm(forms.ModelForm):
#     # Connect form class to model class by defining a nested/inner class. 
#     class Meta:
#         model = Participant
#         fields = ['email']


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')
