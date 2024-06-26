from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from website.models import Funcionario
from website.forms import InsereFuncionarioForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionario")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")

