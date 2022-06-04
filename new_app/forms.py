from django import forms
from django.core.exceptions import ValidationError

from new_app.models import Person



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
