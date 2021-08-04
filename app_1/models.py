from django.db import models
import datetime

#  CLients
class Client(models.Model):

    client = models.ForeignKey("ClientInfo", blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Имя клиента')

    contract_create_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата закл. договора')
    
    contract_end_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата заверш. договора')
    
    contract_desc = models.CharField(blank=True, null=True, max_length=155, verbose_name='Коментарий к договору')

    kofa = models.CharField(blank=True, null=True, max_length=50, verbose_name='Вид деятельности')
    
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name='Город')
    
    street = models.CharField(blank=True, null=True, max_length=100, verbose_name='Улица')
    
    cashbox_numb = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Номер кассы')
    
    cashbox_name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Модель кассы')
    
    reg_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата рег. кассы')
    
    end_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата кон. кассы')
    
    iep = models.ForeignKey("IndEntr", blank=True, null=True, on_delete=models.SET_NULL, verbose_name='ИП Кассы')
    
    term_numb = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Номер терминала')
    
    payment = models.IntegerField(blank=True, null=True, default=0, verbose_name='Оплата')
 
    def save(self, *args, **kwargs):
        if self.reg_date:
            self.end_date = self.reg_date + datetime.timedelta(days=330)
            super(Client, self).save(*args, **kwargs)

    class Meta:
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        


# ClientInfo 
class ClientInfo(models.Model):

    name = models.CharField(blank=True, null=True, max_length=155, verbose_name='Имя')
    tel_number = models.CharField(blank=True, null=True, max_length=13, verbose_name='Тел.')
    email = models.EmailField(blank=True, null=True, max_length=50, verbose_name='Почта')

    class Meta:
        db_table = 'client_info'
        verbose_name = 'Клиент (имя,тел.,почта)'
        verbose_name_plural = 'Клиент (имя,тел.,почта)'
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} - {self.tel_number}"



# Individual Entrpreneur
class IndEntr(models.Model):

    TYPE_OF_ACTIVITY = (
        ('Одиночка', 'Одиночка'),
        ('Цветы','Цветы'),
        ('СМЦ','СМЦ'),
        ('Солдат','Солдат'),
        ('Цветы солдат','Цветы солдат'),
    )

    full_name = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Ф.И.О')
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
        ('Сбербанк','Сбербанк'),
        ('Альфа-Банк','Альфа-Банк'),
        ('Точка','Точка'),
        ('Райффайзен','Райффайзен'),
        ('Тинькофф','Тинькофф'),
        ('ВТБ','ВТБ'),
    )
    
    create_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата создания')
    login = models.CharField(blank=True, null=True, max_length=50, verbose_name='Логин')
    password = models.CharField(blank=True, null=True, max_length=50, verbose_name='Пароль')
    bank = models.CharField(blank=True, null=True, choices=BANK, max_length=50, verbose_name='Банк')
    card = models.CharField(blank=True, null=True, max_length=50, verbose_name='Карта')
    codeword = models.CharField(blank=True, null=True, max_length=50, verbose_name='Кодовое слово')
    iep = models.ForeignKey("IndEntr", blank=True, null=True, on_delete=models.SET_NULL, verbose_name='ИП')

    class Meta:
        db_table = 'ind_entr_info'
        verbose_name = 'ИП (Банк)'
        verbose_name_plural = 'ИП (Банки)'
        ordering = ['iep']

    def __str__(self):
        return f"{self.iep} - {self.bank}"

