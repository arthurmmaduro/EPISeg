from django.contrib import admin
from colaboradores.models import Colaborador
from colaboradores.forms import ColaboradorAdminForm

# Register your models here.
@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    form = ColaboradorAdminForm
    list_display = ['nome', 'cpf', 'data_nascimento', 'cargo', 'email', 'telefone']
    search_fields = ['nome', 'email']
    list_filter = ['cargo']
