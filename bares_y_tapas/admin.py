from django.contrib import admin
from bares_y_tapas.models import *

class BarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Bar, BarAdmin)
admin.site.register(Tapa)
