from dataclasses import fields
from dataclasses import fields
from django import forms
from .import models
class bookform(forms.ModelForm):
    class Meta:
        model=models.bookmodel
        fields="__all__"
