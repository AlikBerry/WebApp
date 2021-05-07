from django.db import models
import datetime

#  CLients
class Client(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Имя')
    tel_number = models.CharField(blank=True, null=True, max_length=11, verbose_name='Тел.')
    email = models.EmailField(blank=True, null=True, max_length=50, verbose_name='Почта')
    monthly_payment = models.PositiveIntegerField(blank=True, null=True, verbose_name='Ежемесячная оплата')
    address = models.ForeignKey("Address", on_delete=models.DO_NOTHING, verbose_name='Адрес')
    kofa = models.ForeignKey("KindOfActivity", on_delete=models.DO_NOTHING, verbose_name='Вид деятельности')    

    class Meta:
        db_table = 'client'
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ['-kofa_id']
    
    def __str__(self):
        return f'{self.name} - {self.tel_number} - {self.address_id} - {self.kofa_id}'
        
# Adresses
class Address(models.Model):
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name='Город')
    street = models.CharField(blank=True, null=True, unique=True, max_length=100, verbose_name='Улица')
    
    class Meta:
        db_table = 'address'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['city', 'street']
    
    def __str__(self):
        return f'{self.city},{self.street}'
    
# Kind_of_activity Clients
class KindOfActivity(models.Model):
    kofa = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Вид деятельности')

    class Meta:
        db_table = 'kind_of_activity'
        verbose_name = 'Клиент (вид деятельности клиента)'
        verbose_name_plural = 'Клиенты (виды деятельности клиентов)'
        ordering = ['kofa']
    
    def __str__(self):
        return f'{self.kofa}'

# Terminals
class Terminals(models.Model):
    term_numb = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Номер терминала')
    client = models.ForeignKey("Client", on_delete=models.DO_NOTHING, verbose_name='Клиент')
    
    class Meta:
        db_table = 'terminals'
        verbose_name = 'Терминал'
        verbose_name_plural = 'Терминалы'
        ordering = ['client_id']
    
    def __str__(self):
        return f'{self.term_numb} - {self.client_id}'

   
# Cashboxes
class Cashboxes(models.Model):
  
    CASHB_NAME = (
        ('Merkury_115F','Merkury-115F'),
        ('Merkury_185F','Merkury-185F'),
        ('SHTRIX_M','SHTRIX-M'),
        ('ATOL','Atol'),
    )

    reg_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата регистрации')
    end_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата окончания')
    cashb_name = models.CharField(blank=True, null=True, choices=CASHB_NAME, max_length=50, verbose_name='Модель кассы')
    ident_numb = models.CharField(blank=True, null=True, unique=True, max_length=50, verbose_name='Номер кассы')
    iep = models.ForeignKey("IndEntr", on_delete=models.DO_NOTHING, verbose_name='ИП')
    client = models.ForeignKey("Client", on_delete=models.DO_NOTHING, verbose_name='Клиент')

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



# Individual Entrpreneur
class IndEntr(models.Model):

    TYPE_OF_ACTIVITY = (
        ('SOLDAT', 'Soldat'),
        ('CHISTIY','Chistiy'),
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
        verbose_name = 'Индивидуальный Предпрениматель'
        verbose_name_plural = 'Индивидуальные Предпрениматели'
        ordering = ['type_of_activity']
    
    def __str__(self):
        return f'{self.full_name} - {self.type_of_activity}'


# Individual Entrpreneur Info
class IndEntrInfo(models.Model):


    BANK = (
        ('Sberbank','Sberbank'),
        ('Tinkoff','Tinkoff'),
        ('Tochka','Tochka'),
    )
    
    create_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Дата создания')
    login = models.CharField(blank=True, null=True, max_length=50, verbose_name='Логин')
    password = models.CharField(blank=True, null=True, max_length=50, verbose_name='Пароль')
    bank = models.CharField(blank=True, null=True, choices=BANK, max_length=50, verbose_name='Банк')
    card = models.CharField(blank=True, null=True, max_length=50, verbose_name='Карта')
    codeword = models.CharField(blank=True, null=True, max_length=50, verbose_name='Кодовое слово')
    iep = models.ForeignKey("IndEntr", on_delete=models.DO_NOTHING, verbose_name='ИП')

    class Meta:
        db_table = 'ind_entr_info'
        verbose_name = 'Инфо. Индивидуального Предпренимателя'
        verbose_name_plural = 'Инфо. Индивидуальных Предпренимателей'
        ordering = ['bank']

    def __str__(self):
        return f'{self.iep_id} - {self.bank}'




