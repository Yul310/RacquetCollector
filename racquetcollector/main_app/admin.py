from django.contrib import admin

# Register your models here.
# import your models here
from .models import Racquet,Restring

# Register your models here
admin.site.register(Racquet)
admin.site.register(Restring)