from django.contrib import admin
from django.db import models
from . models import farmer,farm

# Register your models here.
admin.site.register(farmer)
admin.site.register(farm)
