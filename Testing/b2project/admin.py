from django.contrib import admin
from . models  import Feature 
from . models import Contract
<<<<<<< HEAD
from . models import UserProfile
=======
>>>>>>> 2747631b43589992519fc4336e12ef81ea50be47

# Register your models here.
# After created Database from models, import Database here and Register here, 
# then the data wil go to Django backend database


admin.site.register(Feature)
admin.site.register(Contract)
<<<<<<< HEAD
admin.site.register(UserProfile)
=======
>>>>>>> 2747631b43589992519fc4336e12ef81ea50be47
