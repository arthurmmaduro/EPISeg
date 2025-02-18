from django.contrib import admin
from epis.models import EPIs

# Register your models here.

@admin.register(EPIs)
class EPIsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo', 'fabricante', 'numero_ca', 'categoria', 'validade_ca')
    list_filter = ('categoria', 'fabricante', 'validade_ca')
    search_fields = ('nome', 'modelo', 'fabricante', 'numero_ca')
    prepopulated_fields = {'slug': ('numero_ca',)}
    ordering = ('nome',)
    date_hierarchy = 'validade_ca'