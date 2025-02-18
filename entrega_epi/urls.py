from django.urls import path
from entrega_epi.views import MostrarListaColaboradoresView, AdicionarEPIView,LimparEntregasView, GerarFormularioEPIView,ApagarFichaEPIView, FichaRecenteAPI

urlpatterns = [
    path('', MostrarListaColaboradoresView.as_view(), name='entrega_lista'),
    path('adicionar_epi/<slug:slug>/', AdicionarEPIView.as_view(), name='adicionar_epi'),
    path('limpar_entregas/<slug:slug>/', LimparEntregasView.as_view(), name='limpar_entregas'),
    path('gerar_formulario/<slug:slug>/', GerarFormularioEPIView.as_view(), name='gerar_formulario'),
    path('ficha/apagar/<int:ficha_id>/', ApagarFichaEPIView.as_view(), name='ficha_apagar'),
    path('ficha-recente/<slug:colaborador_slug>/', FichaRecenteAPI.as_view(), name='ficha_recente_api'),
]
