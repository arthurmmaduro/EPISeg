from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from colaboradores.models import Colaborador
from colaboradores.forms import ColaboradorForm

# Create your views here.

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaboradores/colaboradores_lista.html'
    context_object_name = 'colaboradores'

class ColaboradorDetailView(DetailView):
    model = Colaborador
    template_name = 'colaboradores/colaborador_detalhes.html'
    context_object_name = 'colaborador'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Colaborador, slug=slug)

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaboradores/colaborador_adicionar.html'
    success_url = reverse_lazy('colaboradores_lista')
    
    def form_invalid(self, form):
        print(form.errors)  # Mostra os erros do formulário no console
        return self.render_to_response(self.get_context_data(form=form))

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaboradores/colaborador_adicionar.html'
    context_object_name = 'colaborador'
    success_url = reverse_lazy('colaboradores_lista')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaboradores/colaborador_confirm_delete.html'
    context_object_name = 'colaborador'
    success_url = reverse_lazy('colaboradores_lista')
