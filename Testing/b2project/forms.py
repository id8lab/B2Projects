from django.forms import ModelForm
from .models import Contract    # importing Contract from models.py

class contractForm(ModelForm):  # Display the Contract from models.py
    class Meta:
        model = Contract
        fields = '__all__'  # Display all fields from Contract Class

"""
from django import forms

class createcontract(forms.Form):
    name = forms.CharField()    # Contract Name
    description = forms.CharField(widget = forms.Textarea (label = 'Contract Description')) # Contract Description
    task = forms.CharField(label = 'Task Description')  # Contract Tasks
    duration = forms.DateField(label = 'Task Duration') # Contract Duration
"""