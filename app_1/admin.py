from django.contrib import admin
from app_1.models import Client, ClientInfo, Address, Cashboxes, Terminals, KindOfActivity, IndEntr, IndEntrInfo, Contract, CashbName
from import_export.admin import ImportExportModelAdmin








@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["address", "cashbox", "kofa", "client", "contract", "payment"]
    search_fields = ["address__street", "cashbox__ident_numb"]
    autocomplete_fields = ["kofa", "address", "cashbox", "client"]
    list_filter = ("kofa",)


@admin.register(ClientInfo)
class ClientInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["name", "tel_number", "email"]
    search_fields = ["name", "tel_number"]
    

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["city", "street"]
    search_fields = ["city", "street"]


@admin.register(Cashboxes)
class CashboxesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["reg_date", "end_date", "cashb_name", "ident_numb", "iep"]
    search_fields = ["cashb_name__cashb_name", "ident_numb", "iep__full_name"]
    autocomplete_fields = ["iep", "cashb_name"]
    
    

@admin.register(Terminals)
class TerminalsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["term_numb"]
    search_fields = ["term_numb"]
    

@admin.register(Contract)
class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["create_date", "end_date", "desc"]
    search_fields = ["desc"]


@admin.register(KindOfActivity)
class KindOfActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["kofa"]
    search_fields = ["kofa"]


@admin.register(CashbName)
class CashbNameAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["cashb_name"]
    search_fields = ["cashb_name"]    


@admin.register(IndEntr)
class IndEntrAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["reg_date", "full_name", "ident_number", "type_of_activity", "tel_number", "channel", "el_key", "status"]
    search_fields = ["full_name", "ident_number"]
    list_filter = ("type_of_activity", "status")


@admin.register(IndEntrInfo)
class IndEntrInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["iep", "bank", "card"]
    search_fields = ["iep__full_name"]
    autocomplete_fields = ["iep"]
    list_filter = ("bank",)

# admin.site.register(Address)
# admin.site.register(Cashboxes)
# admin.site.register(Terminals)
# admin.site.register(KindOfActivity)
# admin.site.register(IndEntr)
# admin.site.register(IndEntrInfo)
