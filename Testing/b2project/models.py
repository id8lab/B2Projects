from django.db import models

# Create your models here.
# Create Database modle here 
# Building Databse using Python classes which is from views.py

#Every time we add data or change here. After that, do 2 steps: make mirgrate and migraton on shell or bash

class Feature(models.Model):
    name = models.CharField (max_length = 100)
    details = models.CharField (max_length = 500)