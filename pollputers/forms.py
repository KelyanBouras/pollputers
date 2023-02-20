from django import forms
from .models import *


# creating a form
class Processform(forms.ModelForm):  # a form that will be used to create 'Processor' in the database
    class Meta:
        # specify model to be used
        model = Processor

        # specify fields to be used
        fields = [
            "name"
        ]
