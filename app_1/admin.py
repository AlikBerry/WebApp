from django.contrib import admin
from app_1.models import Client, Address, Cashboxes, CashboxName, Terminal, KindOfActivity

admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Cashboxes)
admin.site.register(CashboxName)
admin.site.register(Terminal)
admin.site.register(KindOfActivity)
