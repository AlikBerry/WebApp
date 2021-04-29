from django.db import models

import datetime



class Client(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    tel_number = models.CharField(blank=True, null=True, max_length=11)
    email = models.EmailField(blank=True, null=True, max_length=50)
    monthly_payment = models.PositiveIntegerField(blank=True, null=True)
    address_id = models.ForeignKey("Address", on_delete=models.DO_NOTHING)
    kofa_id = models.ForeignKey("KindOfActivity", on_delete=models.DO_NOTHING)    

    class Meta:
        db_table = 'client'
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ['-kofa_id']
    
    def __str__(self):
        return f'{self.name} - {self.tel_number} - {self.address_id} - {self.kofa_id}'
        

class Address(models.Model):
    city = models.CharField(blank=True, null=True, max_length=50)
    street = models.CharField(blank=True, null=True, unique=True, max_length=100)
    
    class Meta:
        db_table = 'address'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['city', 'street']
    
    def __str__(self):
        return f'{self.city},{self.street}'
    
    
class KindOfActivity(models.Model):
    kofa = models.CharField(blank=True, null=True, unique=True, max_length=50)

    class Meta:
        db_table = 'kind_of_activity'
        verbose_name = 'Вид деятельности клиента'
        verbose_name_plural = 'Виды деятельности клиента'
        ordering = ['kofa']
    
    def __str__(self):
        return f'{self.kofa}'


class Terminals(models.Model):
    term_numb = models.CharField(blank=True, null=True, unique=True, max_length=50)
    client_id = models.ForeignKey("Client", on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'terminals'
        verbose_name = 'Терминал'
        verbose_name_plural = 'Терминалы'
        ordering = ['client_id']
    
    def __str__(self):
        return f'{self.term_numb} - {self.client_id}'

   

class Cashboxes(models.Model):
  
    CASHB_NAME = (
        ('Merkury_115F','Merkury-115F'),
        ('Merkury_185F','Merkury-185F'),
        ('SHTRIX_M','SHTRIX-M'),
        ('ATOL','Atol'),
    )

    reg_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    cashb_name = models.CharField(blank=True, null=True, choices=CASHB_NAME, max_length=50)
    ident_numb = models.CharField(blank=True, null=True, unique=True, max_length=50)
    iep_id = models.ForeignKey("IndEntr", on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey("Client", on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.end_date = self.reg_date + datetime.timedelta(days=330)
        super(Cashboxes, self).save(*args, **kwargs)

    class Meta:
        db_table = 'cashboxes'
        verbose_name = 'Касса'
        verbose_name_plural = 'Кассы'
        ordering = ['cashb_name']
    
    def __str__(self):
        return f'{self.cashb_name} - {self.ident_numb} - {self.iep_id} - {self.client_id}'



    
class IndEntr(models.Model):

    TYPE_OF_ACTIVITY = (
        ('SOLDAT', 'Soldat'),
        ('CHISTIY','Chistiy'),
    )

    full_name = models.CharField(blank=True, null=True, max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(blank=True, null=True, max_length=100)
    ident_number = models.CharField(blank=True, null=True, max_length=12)
    tel_number = models.CharField(blank=True, null=True, max_length=11)
    channel = models.CharField(blank=True, null=True, max_length=2)
    el_key = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    type_of_activity = models.CharField(blank=True, null=True, choices=TYPE_OF_ACTIVITY, max_length=50)
    reg_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)

    def save(self, *args, **kwargs):
        self.end_date = self.reg_date + datetime.timedelta(days=330)
        super(IndEntr, self).save(*args, **kwargs)

    class Meta:
        db_table = 'ind_entr'
        verbose_name = 'Индивидуальный Предпрениматель'
        verbose_name_plural = 'Индивидуальные Предпрениматели'
        ordering = ['type_of_activity']
    
    def __str__(self):
        return f'{self.full_name}'
 