from django.urls import path
from epis.views import ListaEPIsView, CadastrarEPIView,VisualizarEPIView, EditarEPIView, ExcluirEPIView, importar_epis

urlpatterns = [
    path('', ListaEPIsView.as_view(), name='epis_lista' ),
    path('adicionar/', CadastrarEPIView.as_view(), name='epi_adicionar'),
    path('<slug:slug>', VisualizarEPIView.as_view(), name='epi_detalhes'),
    path('editar/<slug:slug>', EditarEPIView .as_view(), name='epi_editar'),
    path('excluir/<slug:slug>', ExcluirEPIView.as_view(), name='epi_excluir'),
    path('importar/', importar_epis, name='epi_importar'),
]