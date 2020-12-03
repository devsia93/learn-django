from django import forms
from .models import *


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['name', 'city']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }