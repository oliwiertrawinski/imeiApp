from django.contrib.gis.db.models import PointField
from django.db import models
from django.contrib import auth
from datetime import datetime
#from geoposition.fields import GeopositionField
from django.utils import timezone

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Phone_brands(models.Model):

    objectId =  models.CharField(max_length=100, unique=True, null=False)
    Model = models.CharField(max_length=100,  null=False)
    Brand = models.CharField(max_length=100,  null=False)
    Network = models.CharField(max_length=100)
    TwoG = models.CharField(max_length=100)
    ThreeG = models.CharField(max_length=100)
    FourG = models.CharField(max_length=100)
    Network_Speed = models.CharField(max_length=100)
    GPRS = models.CharField(max_length=100)
    EDGE = models.CharField(max_length=100)
    Announced = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Dimensions = models.CharField(max_length=100)
    field13 = models.CharField(max_length=100)
    SIM = models.CharField(max_length=100)
    Display_type = models.CharField(max_length=100)
    Display_resolution = models.CharField(max_length=100)
    Display_size = models.CharField(max_length=100)
    Operating_System = models.CharField(max_length=100)
    CPU = models.CharField(max_length=100)
    Chipset = models.CharField(max_length=100)
    GPU = models.CharField(max_length=100)
    Memory_card = models.CharField(max_length=100)
    Internal_memory = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    Primary_camera = models.CharField(max_length=100)
    Secondary_camera = models.CharField(max_length=100)
    Loud_speaker = models.CharField(max_length=100)
    Audio_jack = models.CharField(max_length=100)
    WLAN = models.CharField(max_length=100)
    Bluetooth = models.CharField(max_length=100)
    GPS = models.CharField(max_length=100)
    NFC = models.CharField(max_length=100)
    Radio = models.CharField(max_length=100)
    USB = models.CharField(max_length=100)
    Sensors = models.CharField(max_length=100)
    Battery = models.CharField(max_length=100)
    Colors = models.CharField(max_length=100)
    createdAt = models.CharField(max_length=100)
    updatedAt = models.CharField(max_length=100)

    def __str__(self):
        return  self.Brand + " " +self.Model


class Imei_numbers(models.Model):
    Id = models.AutoField(primary_key=True)
    ImeiNumber = models.CharField(max_length = 100, unique=True, null=False)
    IdPhoneModel = models.ForeignKey(Phone_brands, on_delete=models.CASCADE, related_name="phone_brand", null=False, db_constraint=False)

    def __str__(self):
        return self.ImeiNumber + " " + str(self.IdPhoneModel)

# class Stolen_phones()

class Stolen_markers(models.Model):
    """A marker with name and location."""
    owner = models.ForeignKey(auth.models.User, on_delete=models.PROTECT, related_name="owner", null=False, db_constraint=False)
    imei = models.ForeignKey(Imei_numbers, on_delete=models.CASCADE, related_name="stolen_phone", null=False, db_constraint=False)
    location = PointField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"Name: {self.owner}; imei: {self.imei.ImeiNumber}; location: {self.location}"