from django.db import models

# Create your models here.
# Create Database modle here 
# Building Databse using Python classes whihc is from views.py

#Every time we add data or change here. After that, do 2 steps: make mirgrate and migraton on shell or bash

class Feature(models.Model):
    name = models.CharField (max_length = 100)
    details = models.CharField (max_length = 500)

class UserProfile(models.Model): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    bank_info = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=25)

    def __str__(self):
      return self.first_name   


class Contract(models.Model):   # Contract Template.
    ContractName = models.CharField (max_length = 100)
    ContractDescription = models.TextField (max_length = 40000)
    ContractTasks = models.TextField (max_length = 40000)
    StartDate = models.DateTimeField('Start Date', max_length=8)
    EndDate = models.DateTimeField ('End Date', max_length=8)
    Payment = models.TextField (max_length = 40000, default = "")
    SalaryStatement = models.ImageField(null=True, blank=True, upload_to='images/') # storing images to folder: images
    
    #user_name = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
      return self.ContractName

"""
class SalaryStatement(models.Model):
    title = models.CharField(max_length=4000)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
"""

