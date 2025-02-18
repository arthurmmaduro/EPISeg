from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from autenticacao.models import CustomUser  

# Modelo Colaborador
class Colaborador(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF', blank=True, null=True)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    slug = models.SlugField(unique=True, blank=True)
    
    # Relacionamento com o CustomUser
    usuario = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='colaborador', 
        null=True, 
        blank=True
    )
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        
        if not self.usuario and CustomUser.objects.filter(email=self.email).exists():
            raise ValidationError("Já existe um usuário com este e-mail.")

        if not self.usuario:
            user = CustomUser.objects.create_user(
                email=self.email,
                password='senha123'  # Senha padrão (você pode alterar isso depois)
            )
            self.usuario = user
            
        super().save(*args, **kwargs)

    @property
    def primeiro_nome(self):
        return self.nome.split(' ')[0]
    
    def delete(self, *args, **kwargs):
        usuario = self.usuario  # Obtém o usuário associado
        super().delete(*args, **kwargs)  # Exclui o colaborador
        if usuario:
            usuario.delete()  # Exclui o usuário associado

    def __str__(self):
        return self.nome
