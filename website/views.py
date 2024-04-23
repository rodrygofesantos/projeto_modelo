from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from website.models import Funcionario
from website.forms import InsereFuncionarioForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

# Cada método que tiver esse decorator, vai exigir login para acessar
# Caso não precise de login, basta remover
# Existe uma forma de fazer o inverso, dizer que todos precisa e apenas sinalizar os que não precisam
# Mas isso exigiria a utilização/criação de um middleware
# Outra coisa, se ao invés de CBV fosse FBV, bastaria utilizar a seguinte anotação:
# @login_required
# def meu_metodo(request):
#     ...
@method_decorator(login_required, name='dispatch')
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

@method_decorator(login_required, name='dispatch')
class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

@method_decorator(login_required, name='dispatch')
class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionario")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

@method_decorator(login_required, name='dispatch')
class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

@method_decorator(login_required, name='dispatch')
class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")

