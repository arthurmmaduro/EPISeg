from django.urls import path
from colaboradores.views import ColaboradorListView, ColaboradorDetailView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView


urlpatterns = [
    path('', ColaboradorListView.as_view(), name='colaboradores_lista'),
    path('adicionar/', ColaboradorCreateView.as_view(), name='colaborador_adicionar'),
    path('<slug:slug>/', ColaboradorDetailView.as_view(), name='colaborador_detalhes'),
    path('editar/<slug:slug>/', ColaboradorUpdateView.as_view(), name='colaborador_editar'),
    path('excluir/<slug:slug>/', ColaboradorDeleteView.as_view(), name='colaborador_excluir'),
]
