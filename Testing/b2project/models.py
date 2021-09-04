from django.db import models
# Create your models here.
# Create Database modle here 
# Building Databse using Python classes whihc is from views.py

#Every time we add data or change here. After that, do 2 steps: make mirgrate and migraton on shell or bash

class Feature(models.Model):
    name = models.CharField (max_length = 100)
    details = models.CharField (max_length = 500)


class Contract(models.Model):   # Contract Template.
  ContractName = models.CharField (max_length = 100)
  ContractDescription = models.CharField (max_length = 4000, default="Enter Contract Description")
  ContractTasks = models.CharField (max_length = 40000, default = "Enter Contract Tasks")
  StartDate = models.CharField (max_length = 6, default = "Enter Start Date DDMMYY")
  EndDate = models.CharField (max_length = 6, default = "Enter End Date DDMMYY")
