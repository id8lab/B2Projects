#from django import form
from django import forms
from django.forms import ModelForm  #Add data to our database
from .models import Contract, SalaryStatement    # importing Contract from models.py
from .models import *

#Create Contract forms
class contractForm(ModelForm):  # Display the Contract from models.py
    class Meta:
        model = Contract
        fields = ('ContractName', 'ContractDescription', 'ContractTasks', 'StartDate', 'EndDate', 'Payment')  # Display all fields from Contract Class
        
        labels = {
            'ContractName': '', 
            'ContractDescription': '',
            'ContractTasks': '',
            'StartDate': '',
            'EndDate': '',
            'Payment Amount': '',
        }


        widgets = {
            'ContractName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Name'}),
            'ContractDescription': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Description'}),
            'ContractTasks': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Tasks'}),
            'StartDate': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            'EndDate': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'End Date'}),
            'Payment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Payment Amount'}),
        }
# image handling form
class SalaryStatementForm(forms.ModelForm):
    class Meta:
        model = SalaryStatement
        fields = ('title', 'image')

"""
from django import forms

class createcontract(forms.Form):
    name = forms.CharField()    # Contract Name
    description = forms.CharField(widget = forms.Textarea (label = 'Contract Description')) # Contract Description
    task = forms.CharField(label = 'Task Description')  # Contract Tasks
    duration = forms.DateField(label = 'Task Duration') # Contract Duration
"""