from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import FileResponse,JsonResponse
from django.views.generic import TemplateView,View
import requests
from colaboradores.models import Colaborador
from entrega_epi.models import EntregaColaboradorEPI, FichaEPI

# Create your views here.

class PerfilView(TemplateView):
    template_name = 'perfil/perfil.html'

    def get_context_data(self, **kwargs):
        # Obtém o contexto padrão
        context = super().get_context_data(**kwargs)

        # Busca o colaborador logado
        colaborador = get_object_or_404(Colaborador, email=self.request.user.email)
        context['colaborador'] = colaborador

        # Busca os EPIs entregues ao colaborador
        entregas = EntregaColaboradorEPI.objects.filter(colaborador=colaborador).select_related('epi')
        context['epis'] = [entrega.epi for entrega in entregas]

        # Busca diretamente a ficha mais recente no banco de dados
        ficha_recente = FichaEPI.objects.filter(colaborador=colaborador).order_by('-data_geracao').first()
        context['ficha_recente'] = ficha_recente

        return context


    
class BaixarFichaEPIView(View):
    def get(self, request, ficha_id, *args, **kwargs):
        ficha = get_object_or_404(FichaEPI, id=ficha_id)
        if not ficha.arquivo:
            return JsonResponse({'status': 'error', 'message': 'Arquivo não encontrado'}, status=404)

        return FileResponse(ficha.arquivo.open(), as_attachment=True, filename=ficha.arquivo.name)
    
