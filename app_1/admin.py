from django.contrib import admin
from app_1.models import Client, Address, Cashboxes, Terminals, KindOfActivity, IndEntr, IndEntrInfo
from import_export.admin import ImportExportModelAdmin



@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["name", "tel_number"]
    autocomplete_fields = ["kofa", "address"]

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["city", "street"]

@admin.register(Cashboxes)
class CashboxesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["cashb_name", "ident_numb"]
    autocomplete_fields = ["iep", "client"]

@admin.register(Terminals)
class TerminalsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["term_numb"]
    autocomplete_fields = ["client"]

@admin.register(KindOfActivity)
class KindOfActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["kofa"]


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
