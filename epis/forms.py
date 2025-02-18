from django import forms
from epis.models import EPIs

class EPIForm(forms.ModelForm):
        class Meta:
            model = EPIs
            fields = [
                'nome',
                'modelo',
                'fabricante',
                'descricao',
                'numero_ca',
                'arquivo_ca',
                'categoria',
                'validade_ca',
            ]
            labels = {
                'nome': 'Equipamento de Proteção Individual',
                'modelo': 'Modelo',
                'fabricante': 'Fabricante',
                'descricao': 'Descrição',
                'numero_ca': 'Número do CA',
                'arquivo_ca': 'Arquivo do CA',
                'categoria': 'Categoria',
                'validade_ca': 'Validade do CA',
            }
            
            widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do EPI'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o modelo'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o fabricante'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Digite uma descrição'}),
            'numero_ca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número do CA'}),
            'arquivo_ca': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'validade_ca': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ImportEPIForm(forms.Form):
    arquivo = forms.FileField(
        label="Selecione o arquivo Excel (.xls ou .xlsx)",
        help_text="O arquivo deve conter as colunas esperadas: EPI, Modelo, Fabricante, Número CA, etc."
    )