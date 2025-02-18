from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
import pandas as pd
import openpyxl
from epis.models import EPIs
from epis.forms import EPIForm, ImportEPIForm

# Create your views here.

class ListaEPIsView(ListView):
    model = EPIs
    template_name = 'epis/epis_lista.html'
    context_object_name = 'epis'

class CadastrarEPIView(CreateView):
    model = EPIs
    form_class = EPIForm
    template_name = 'epis/epi_adicionar.html'
    context_object_name = 'epi'
    success_url = reverse_lazy('epis_lista')

    def form_valid(self, form):
        print("Formulário válido:", form.cleaned_data)  # Verifica os dados válidos
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Formulário inválido:", form.errors)  # Exibe erros de validação
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        print("POST Data:", request.POST)  # Dados enviados
        print("FILES Data:", request.FILES)  # Arquivos enviados
        return super().post(request, *args, **kwargs)

class VisualizarEPIView(DetailView):
    model = EPIs
    template_name = 'epis/epis_detalhes.html'
    context_object_name = 'epi'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return EPIs.objects.get(slug=slug)
    
class EditarEPIView(UpdateView):
    model = EPIs
    fields = ['nome', 'modelo', 'fabricante', 'descricao', 'numero_ca', 'arquivo_ca', 'categoria', 'validade_ca']
    template_name = 'epis/epi_adicionar.html'
    context_object_name = 'epi'
    success_url = reverse_lazy('epis_lista')
    
class ExcluirEPIView(View):
    def post(self, request, slug):
        colaborador = get_object_or_404(EPIs, slug=slug)
        
        colaborador.delete()
        
        return redirect('epis_lista')
    
def importar_epis(request):
    if request.method == 'POST':
        form = ImportEPIForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            try:
                # Ler o arquivo Excel
                dados = pd.read_excel(arquivo)

                # Verificar se as colunas esperadas estão presentes
                colunas_esperadas = ['EPI', 'Fabricante', 'Modelo', 'CA da Etiqueta', 'Validade do CA']
                if not all(col in dados.columns for col in colunas_esperadas):
                    messages.error(request, "Erro: O arquivo não contém todas as colunas obrigatórias.")
                    return render(request, 'epis/epi_importar.html', {'form': form})

                # Iterar pelas linhas do DataFrame e criar ou atualizar EPIs
                for _, linha in dados.iterrows():
                    EPIs.objects.update_or_create(  
                        numero_ca=linha['CA da Etiqueta'],
                        defaults={
                            'nome': linha['EPI'],
                            'fabricante': linha['Fabricante'],
                            'modelo': linha['Modelo'],
                            'validade_ca': linha['Validade do CA'],
                        }
                    )

                messages.success(request, "Importação concluída com sucesso!")
                return redirect('epis_lista')

            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
                return render(request, 'epis/epi_importar.html', {'form': form})
    else:
        form = ImportEPIForm()

    return render(request, 'epis/epi_importar.html', {'form': form})