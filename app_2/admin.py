from django.contrib import admin
from app_2.models import Transacions
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Transacions)
class TransactionsAdmin(ImportExportModelAdmin):
    pass

    
       