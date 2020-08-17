from django.contrib import admin
from .models import Country, City
from import_export.admin import ImportExportModelAdmin


# Register your models here.
# admin.site.register(Country)
# admin.site.register(City)

@admin.register(Country, City)
class ViewAdmin(ImportExportModelAdmin):
    pass
