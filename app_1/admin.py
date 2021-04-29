from django.contrib import admin
from app_1.models import Client, Address, Cashboxes, Terminals, KindOfActivity, IndEntr
from import_export.admin import ImportExportModelAdmin



@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Address)
admin.site.register(Cashboxes)
admin.site.register(Terminals)
admin.site.register(KindOfActivity)
admin.site.register(IndEntr)
