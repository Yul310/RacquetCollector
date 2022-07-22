from django.contrib import admin

# Register your models here.
# import your models here
from .models import Racquet,Restring,User

# Register your models here
admin.site.register(Racquet)
admin.site.register(Restring)
admin.site.register(User)