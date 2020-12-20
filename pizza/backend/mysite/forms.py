from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('title', 'content', 'topings')

        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'topings': forms.SelectMultiple(),
            'slug': forms.TextInput()
        }

    def clean_slug_self(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError(
                'This name for slug should be changed. Name \'create\' already reserved the system.')
        return new_slug


class TopingForm(forms.ModelForm):
    class Meta:
        model = Toping
        fields = ('title', 'content', 'slug')

        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'slug': forms.TextInput()
        }
