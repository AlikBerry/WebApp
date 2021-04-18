from django.db import models
from app_2.models import IndEntr

class Client(models.Model):
    
    name = models.CharField(blank=True, null=True, max_length=50)
    phone_number = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    monthly_payment = models.PositiveIntegerField(blank=True, null=True)
    address_id = models.ForeignKey("Address", on_delete=models.DO_NOTHING)
    kind_of_activity_id = models.ForeignKey("KindOfActivity", on_delete=models.DO_NOTHING)    
    
    def __str__(self):
        return self.name


class Cashboxes(models.Model):
    
    reg_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    cashb_name = models.ForeignKey("CashboxName", on_delete=models.DO_NOTHING)
    ident_numb = models.CharField(blank=True, null=True, max_length=50)
    iep_id = models.ForeignKey("app_2.IndEntr", on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey("Client", on_delete=models.DO_NOTHING)


class Terminal(models.Model):
    
    ter_numb = models.CharField(blank=True, null=True, max_length=50)
    client_id = models.ForeignKey("Client", on_delete=models.DO_NOTHING)

        
class Address(models.Model):
    
    city = models.CharField(blank=True, null=True, max_length=50)
    street = models.CharField(blank=True, null=True, unique=True, max_length=100)
    
    
class CashboxName(models.Model):
    
    name = models.CharField(blank=True, null=True, max_length=50)     
    
    
class KindOfActivity(models.Model):
    
    kind_of_activity = models.CharField(blank=True, null=True, max_length=50)
    

    
    
    
    
