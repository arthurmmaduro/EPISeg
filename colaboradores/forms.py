from django import forms
from colaboradores.models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'data_nascimento', 'cargo', 'email', 'telefone']
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'data_nascimento': 'Data de Nascimento',
            'cargo': 'Cargo',
            'email': 'E-mail',
            'telefone': 'Telefone',
        }
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'})
        }

class ColaboradorAdminForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'data_nascimento', 'cargo', 'email', 'telefone']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'})
        }