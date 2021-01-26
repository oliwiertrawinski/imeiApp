from django.contrib import admin, gis

from imeiApp.models import  User, Imei_numbers, Phone_brands, Stolen_markers

# Register your models here.

admin.site.register(Imei_numbers)
admin.site.register(Phone_brands)

@admin.register(Stolen_markers)
class MarkerAdmin(gis.admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("owner", 'imei', "location")