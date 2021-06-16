from django.contrib import admin
from app_2.models import Transacions
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter

# Register your models here.

@admin.register(Transacions)
class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["create_date", "incoming", "expense", "balance", "desc"]
    search_fields = ["desc", "incoming", "expense"]
    list_filter = (('create_date', DateRangeFilter),)