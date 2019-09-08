from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Subscribers
        exclude=[""]