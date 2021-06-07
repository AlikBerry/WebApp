from django.db import models
from app_1.models import Client
from datetime import *

# Create your models here.

class Transacions(models.Model):

    create_date = models.DateField(blank=True, null=True, default=datetime.now, auto_now=False, auto_now_add=False, verbose_name='Дата')
    incoming = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Приход')
    expense = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Расход')
    balance = models.IntegerField(blank=True, null=True, default=0, verbose_name='Баланс')
    desc = models.CharField(blank=True, null=True, max_length=50, verbose_name='Коментарий')

    def save(self, *args, **kwargs):
        self.balance = self.incoming - self.expense
        super(Transacions, self).save(*args, **kwargs)

    class Meta:
        db_table = 'transactions'
        verbose_name = 'Транзакции'
        verbose_name_plural = 'Транзакции'
        ordering = ['-create_date']
    
    def __str__(self):
        return f"{self.desc}"

