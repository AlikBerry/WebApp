from django.contrib import admin
from app_1.models import Client, ClientInfo, IndEntr, IndEntrInfo
from import_export.admin import ImportExportModelAdmin


@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["client", "city", "street", "cashbox_numb", "cashbox_name",
     "iep", "term_numb", "contract_desc", "kofa", "payment"]

    search_fields = ["city", "street", "iep__full_name", "payment", "client__name"]
    
    autocomplete_fields = ["client", "iep"]
    
    list_filter = ("kofa", "iep__type_of_activity",)



@admin.register(ClientInfo)
class ClientInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ["name", "tel_number", "email"]
    
    search_fields = ["name", "tel_number"]
            
    

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
