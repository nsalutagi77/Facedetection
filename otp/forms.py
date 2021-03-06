from django import forms
from django.contrib.auth import models
from django.forms import fields
from .models import Code

class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter SMS verification code')
    class Meta:
        model = Code
        fields = ('number',)