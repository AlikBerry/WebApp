from django.db import models

class IndEntr(models.Model):

    full_name = models.CharField(blank=True, null=True, max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(blank=True, null=True, max_length=100)
    ident_number = models.CharField(blank=True, null=True, max_length=50)
    tel_number = models.CharField(blank=True, null=True, max_length=11)
    channel = models.CharField(blank=True, null=True, max_length=10)
    el_key = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    type_of_activity = models.ForeignKey("TypeAct", on_delete=models.DO_NOTHING)
    reg_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    
class TypeAct(models.Model):
    
    type_of_activity = models.CharField(blank=True, null=True, max_length=50)
    
    