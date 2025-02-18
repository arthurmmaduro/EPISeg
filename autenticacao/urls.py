from django.urls import path
from autenticacao.views import login_view, logout_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('path', logout_view, name='logout'),
]