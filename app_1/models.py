from django.db import models
import datetime

#  CLients
class Client(models.Model):

    name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Имя')
    tel_number = models.CharField(blank=True, null=True, max_length=13, verbose_name='Тел.')
    email = models.EmailField(blank=True, null=True, max_length=50, verbose_name='Почта')    

    class Meta:
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
    
    
        
# Adresses
class Address(models.Model):

    city = models.CharField(blank=True, null=True, max_length=50, verbose_name='Город')
    street = models.CharField(blank=True, null=True, max_length=100, verbose_name='Улица')
    kofa = models.ForeignKey("KindOfActivity", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Вид деятельности')
    client = models.ForeignKey("Client", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Клиент')

    class Meta:
        db_table = 'address'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['city', 'street']
    
    def __str__(self):
        return f'{self.city},{self.street}'

# Contract
class Contract(models.Model):

    create_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Дата заключения')
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Дата окончания')
    desc = models.CharField(blank=True, null=True, max_length=50, verbose_name='Коментарий')
    address = models.ForeignKey("Address", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Адрес')

    class Meta:
        db_table = 'contract'
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'
        ordering = ['create_date']
    
    def __str__(self):
        return f"{self.desc}"


# Kind_of_activity Clients
class KindOfActivity(models.Model):

    kofa = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Вид деятельности')

    class Meta:
        db_table = 'kind_of_activity'
        verbose_name = 'Клиент (вид деятельности клиента)'
        verbose_name_plural = 'Клиенты (виды деятельности клиентов)'
        ordering = ['kofa']
    
    def __str__(self):
        return f"{self.kofa}"
    

# Terminals
class Terminals(models.Model):

    term_numb = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Номер терминала')
    address = models.ForeignKey("Address", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Адрес')
    
    class Meta:
        db_table = 'terminals'
        verbose_name = 'Терминал'
        verbose_name_plural = 'Терминалы'
        ordering = ['term_numb']
    
  


# Cashboxes Name 
class CashbName(models.Model):
    
    cashb_name = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Модель кассы')

    class Meta:
        db_table = 'cashb_names'
        verbose_name = 'Кассы (модели)'
        verbose_name_plural = 'Кассы (модели)'
        ordering = ['cashb_name']
    
    def __str__(self):
        return f"{self.cashb_name}"
   



# Cashboxes
class Cashboxes(models.Model):
  
    reg_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата регистрации')
    end_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата окончания')
    cashb_name = models.ForeignKey("CashbName", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Модель кассы')
    ident_numb = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Номер кассы')
    iep = models.ForeignKey("IndEntr", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='ИП')
    address = models.ForeignKey("Address", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Адрес')

    def save(self, *args, **kwargs):
        self.end_date = self.reg_date + datetime.timedelta(days=330)
        super(Cashboxes, self).save(*args, **kwargs)

    class Meta:
        db_table = 'cashboxes'
        verbose_name = 'Касса'
        verbose_name_plural = 'Кассы'
        ordering = ['cashb_name']
    
    def __str__(self):
        return f"{self.address}"


# Individual Entrpreneur
class IndEntr(models.Model):

    TYPE_OF_ACTIVITY = (
        ('ОДИНОЧКА', 'Одиночка'),
        ('ЦВЕТЫ','Цветы'),
        ('СМЦ','СМЦ'),
        ('СОЛДАТ','Солдат'),
        ('ЦВЕТЫ СОЛДАТ','Цветы солдат'),
    )

    full_name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Ф.И.О')
    birth_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата рождения')
    address = models.CharField(blank=True, null=True, max_length=100, verbose_name='Адрес регистрации')
    ident_number = models.CharField(blank=True, null=True, max_length=12, verbose_name='ИНН')
    tel_number = models.CharField(blank=True, null=True, max_length=11, verbose_name='Тел.')
    channel = models.CharField(blank=True, null=True, max_length=2, verbose_name='Канал')
    el_key = models.BooleanField(default=True, verbose_name='Электронный ключ')
    status = models.BooleanField(default=True, verbose_name='Статус')
    type_of_activity = models.CharField(blank=True, null=True, choices=TYPE_OF_ACTIVITY, max_length=50, verbose_name='Тип')
    email = models.EmailField(blank=True, null=True, max_length=100, verbose_name='Почта')
    password = models.CharField(blank=True, null=True, max_length=50, verbose_name='Пароль от почты')
    reg_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата регистрации')
    end_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата окончания')

    def save(self, *args, **kwargs):
        self.end_date = self.reg_date + datetime.timedelta(days=330)
        super(IndEntr, self).save(*args, **kwargs)

    class Meta:
        db_table = 'ind_entr'
        verbose_name = 'ИП'
        verbose_name_plural = 'ИП'
        ordering = ['type_of_activity']
    
    def __str__(self):
        return f'{self.full_name}'


# Individual Entrpreneur Info
class IndEntrInfo(models.Model):


    BANK = (
        ('СБЕРБАНК','Сбербанк'),
        ('АЛЬФАБАНК','Альфа-Банк'),
        ('ТОЧКАБАНК','Точка'),
        ('РАЙФФАЙЗЕН','Райффайзен'),
        ('ТИНЬКОФФ','Тинькофф'),
        ('ВТБ','ВТБ'),
    )
    
    create_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата создания')
    login = models.CharField(blank=True, null=True, max_length=50, verbose_name='Логин')
    password = models.CharField(blank=True, null=True, max_length=50, verbose_name='Пароль')
    bank = models.CharField(blank=True, null=True, choices=BANK, max_length=50, verbose_name='Банк')
    card = models.CharField(blank=True, null=True, max_length=50, verbose_name='Карта')
    codeword = models.CharField(blank=True, null=True, max_length=50, verbose_name='Кодовое слово')
    iep = models.ForeignKey("IndEntr", blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='ИП')

    class Meta:
        db_table = 'ind_entr_info'
        verbose_name = 'ИП (Банк)'
        verbose_name_plural = 'ИП (Банки)'
        ordering = ['iep']

    def __str__(self):
        return f"{self.iep} - {self.bank}"

