#from django import form
from django import forms
from django.forms import ModelForm  #Add data to our database
from .models import Contract    # importing Contract from models.py

#Create Contract forms
class contractForm(ModelForm):  # Display the Contract from models.py
    class Meta:
        model = Contract
        fields = ('ContractName', 'ContractDescription', 'ContractTasks', 'StartDate', 'EndDate')  # Display all fields from Contract Class
        
        labels = {
            'ContractName': '', 
            'ContractDescription': '',
            'ContractTasks': '',
            'StartDate': '',
            'EndDate': '',
        }


        widgets = {
            'ContractName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Name'}),
            'ContractDescription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Description'}),
            'ContractTasks': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Tasks'}),
            'StartDate': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            'EndDate': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'End Date'}),
        }

        

"""
from django import forms

class createcontract(forms.Form):
    name = forms.CharField()    # Contract Name
    description = forms.CharField(widget = forms.Textarea (label = 'Contract Description')) # Contract Description
    task = forms.CharField(label = 'Task Description')  # Contract Tasks
    duration = forms.DateField(label = 'Task Duration') # Contract Duration
"""