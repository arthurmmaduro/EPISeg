from django.urls import path
from perfil.views import PerfilView

urlpatterns = [
    path('', PerfilView.as_view(), name='perfil'),
    
]