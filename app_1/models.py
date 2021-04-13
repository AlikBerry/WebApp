from django.db import models

class Client(models.Model):
    name = models.models.CharField(blank=True, null=True, max_length=50)
    phone_number = models.PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=50)
    address = models.models.ForeignKey("Address", on_delete=models.DO_NOTHING)
    monthly_payment = models.models.PositiveIntegerField(blank=True, null=True)
    kind_of_activity = models.models.CharField(blank=True, null=True, max_length=100)

    
class Address(models.Model):
    city = models.models.CharField(blank=True, null=True, max_length=50)
    street = models.models.CharField(blank=True, null=True, unique=True, max_length=100)
    
class Casboxes(models.Model):
    pass
    
    
