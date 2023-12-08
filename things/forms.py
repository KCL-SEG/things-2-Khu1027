"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingsForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}
