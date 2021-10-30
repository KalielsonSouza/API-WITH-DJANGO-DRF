from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person
# Register your models here.

@admin.register(Person)
class PersonModelAdmin(ImportExportModelAdmin):
    list_display = ('id','nome','sobrenome','sexo','altura','peso','nascimento','bairro','cidade','estado','numero','idade')

