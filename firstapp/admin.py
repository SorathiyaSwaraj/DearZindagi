from django.contrib import admin

from firstapp.models import *


# Register your models here.
models_list = [CustomUser] 
admin.site.register(models_list)
