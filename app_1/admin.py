from django.contrib import admin
from app_1.models import Client, Address, Cashboxes, Terminals, KindOfActivity, IndEntr, IndEntrInfo, Contract, CashbName
from import_export.admin import ImportExportModelAdmin



@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["name", "tel_number", "email"]
    search_fields = ["name", "tel_number"]
    

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["city", "street", "kofa", "client", "contract"]
    search_fields = ["city", "street"]
    autocomplete_fields = ["client", "kofa", "contract"]


@admin.register(Cashboxes)
class CashboxesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["reg_date", "end_date", "cashb_name", "ident_numb", "iep", "address"]
    search_fields = ["cashb_name", "ident_numb"]
    autocomplete_fields = ["iep", "address", "cashb_name"]
    

@admin.register(Terminals)
class TerminalsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["term_numb", "address"]
    search_fields = ["term_numb"]
    autocomplete_fields = ["address"]
    

@admin.register(Contract)
class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["desc"]


@admin.register(KindOfActivity)
class KindOfActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["kofa"]


@admin.register(CashbName)
class CashbNameAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["cashb_name"]
    search_fields = ["cashb_name"]    


@admin.register(IndEntr)
class IndEntrAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["full_name", "ident_number"]


@admin.register(IndEntrInfo)
class IndEntrInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["iep__full_name"]
    autocomplete_fields = ["iep"]

# admin.site.register(Address)
# admin.site.register(Cashboxes)
# admin.site.register(Terminals)
# admin.site.register(KindOfActivity)
# admin.site.register(IndEntr)
# admin.site.register(IndEntrInfo)
