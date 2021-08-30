from django.contrib import admin
from . models  import Feature 

# Register your models here.
# After created Database from models, import Database here and Register here, 
# then the data wil go to Django backend database


admin.site.register(Feature)

