from django.contrib import admin
from .models import Pendiente

# Register your models here.

class PendienteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)

admin.site.register(Pendiente,PendienteAdmin)