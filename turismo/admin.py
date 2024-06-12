from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import ViajerosResidenciaDestino
from .resources import ViajerosResidenciaDestinoResource

# Register your models here.


class ViajerosResidenciaDestinoAdmin(ImportExportModelAdmin):
    resource_class = ViajerosResidenciaDestinoResource

admin.site.register(ViajerosResidenciaDestino, ViajerosResidenciaDestinoAdmin)

