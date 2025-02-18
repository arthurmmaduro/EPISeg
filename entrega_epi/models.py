from django.db import models
from epis.models import EPIs
from colaboradores.models import Colaborador

class EntregaColaboradorEPI(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='entregas')
    epi = models.ForeignKey(EPIs, on_delete=models.CASCADE, related_name='entregas')
    data_entrega = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('colaborador', 'epi')

    def __str__(self):
        return f'{self.colaborador.nome} - {self.epi.nome}'
    
class FichaEPI(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='fichas_epi')
    data_geracao = models.DateField(auto_now_add=True)
    arquivo = models.FileField(upload_to='fichas_epis/', blank=True, null=True)

    def __str__(self):
        return f'Ficha de {self.colaborador.nome} - {self.data_geracao}'