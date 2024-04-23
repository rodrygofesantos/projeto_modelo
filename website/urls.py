from django.urls.conf import include

from website.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioCreateView, \
    FuncionarioDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # '/'
    path('',
      IndexTemplateView.as_view(),
      name="index" # <<< Adicionar
    ),

    # '/funcionario/cadastrar'
    path('funcionario/cadastrar',
      FuncionarioCreateView.as_view(),
      name="cadastra_funcionario" # <<< Adicionar
    ),

    # '/funcionarios'
    path('funcionarios/',
      FuncionarioListView.as_view(),
      name="lista_funcionario" # <<< Adicionar
    ),

    # '/funcionario/{pk}'
    path('funcionario/<pk>',
      FuncionarioUpdateView.as_view(),
      name="atualiza_funcionario" # <<< Adicionar
    ),

    # '/funcionarios/excluir/{pk}'
    path('funcionario/excluir/<pk>',
      FuncionarioDeleteView.as_view(),
      name="deleta_funcionario" # <<< Adicionar
    ),

    # Estou adicionando (incluindo) as rotas de autenticação do Django, pois elas já tem as views prontas
    path('accounts/', include('django.contrib.auth.urls')),
]