from django.contrib import admin

# Register your models here.

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shops

@admin.register(Shops)
class ShopsAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')