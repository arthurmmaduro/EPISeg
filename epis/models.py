from django.db import models
from django.utils.text import slugify

# Create your models here.

class EPIs(models.Model):
    CATEGORIAS_NR06 = [
        ('proteção_cabeça', 'Proteção da Cabeça'),
        ('proteção_olhos_face', 'Proteção dos Olhos e Face'),
        ('proteção_auditiva', 'Proteção Auditiva'),
        ('proteção_respiratoria', 'Proteção Respiratória'),
        ('proteção_torax', 'Proteção do Tórax'),
        ('proteção_membros_superiores', 'Proteção dos Membros Superiores'),
        ('proteção_membros_inferiores', 'Proteção dos Membros Inferiores'),
        ('proteção_corpo_inteiro', 'Proteção do Corpo Inteiro'),
        ('proteção_contra_quedas', 'Proteção Contra Quedas'),
    ]

    nome = models.CharField(max_length=100, verbose_name='EPI')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    fabricante = models.CharField(max_length=100, verbose_name='Fabricante')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    numero_ca = models.CharField(max_length=20, unique=True, verbose_name='Número do CA')
    arquivo_ca = models.FileField(upload_to='documentos/epis/', blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_NR06, default='', verbose_name='Categoria')
    validade_ca = models.DateField(verbose_name='Validade do CA')
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'EPI'
        verbose_name_plural = 'EPIs'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.numero_ca)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome