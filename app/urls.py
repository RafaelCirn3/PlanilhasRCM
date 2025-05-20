from django.urls import path
from .views import (
    index, home, 
    # SERVIÇO
    ServicoListView, ServicoDetailView, ServicoCreateView,
    ServicoUpdateView, ServicoDeleteView,

    # REGISTRO DE SERVIÇO
    RegistroServicoListView, RegistroServicoDetailView, RegistroServicoCreateView,
    RegistroServicoUpdateView, RegistroServicoDeleteView,

    # INSUMO
    InsumoListView, InsumoDetailView, InsumoCreateView,
    InsumoUpdateView, InsumoDeleteView,

    # MOVIMENTAÇÃO DE INSUMO
    MovimentacaoInsumoListView, MovimentacaoInsumoDetailView, MovimentacaoInsumoCreateView,
    MovimentacaoInsumoUpdateView, MovimentacaoInsumoDeleteView,
    
    # OUTROS
    excel_movimentacoes, excel_registros
)

urlpatterns = [
    path('', home, name='home'),
    # SERVIÇO
    path('servicos/', ServicoListView.as_view(), name='servico_list'),
    path('servicos/<int:pk>/', ServicoDetailView.as_view(), name='servico_detail'),
    path('servicos/novo/', ServicoCreateView.as_view(), name='servico_create'),
    path('servicos/<int:pk>/editar/', ServicoUpdateView.as_view(), name='servico_update'),
    path('servicos/<int:pk>/excluir/', ServicoDeleteView.as_view(), name='servico_delete'),

    # REGISTRO DE SERVIÇO
    path('registros/', RegistroServicoListView.as_view(), name='registroservico_list'),
    path('registros/<int:pk>/', RegistroServicoDetailView.as_view(), name='registroservico_detail'),
    path('registros/novo/', RegistroServicoCreateView.as_view(), name='registroservico_create'),
    path('registros/<int:pk>/editar/', RegistroServicoUpdateView.as_view(), name='registroservico_update'),
    path('registros/<int:pk>/excluir/', RegistroServicoDeleteView.as_view(), name='registroservico_delete'),

    # INSUMO
    path('insumos/', InsumoListView.as_view(), name='insumo_list'),
    path('insumos/<int:pk>/', InsumoDetailView.as_view(), name='insumo_detail'),
    path('insumos/novo/', InsumoCreateView.as_view(), name='insumo_create'),
    path('insumos/<int:pk>/editar/', InsumoUpdateView.as_view(), name='insumo_update'),
    path('insumos/<int:pk>/excluir/', InsumoDeleteView.as_view(), name='insumo_delete'),

    # MOVIMENTAÇÃO DE INSUMO
    path('movimentacoes/', MovimentacaoInsumoListView.as_view(), name='movimentacaoinsumo_list'),
    path('movimentacoes/<int:pk>/', MovimentacaoInsumoDetailView.as_view(), name='movimentacaoinsumo_detail'),
    path('movimentacoes/novo/', MovimentacaoInsumoCreateView.as_view(), name='movimentacaoinsumo_create'),
    path('movimentacoes/<int:pk>/editar/', MovimentacaoInsumoUpdateView.as_view(), name='movimentacaoinsumo_update'),
    path('movimentacoes/<int:pk>/excluir/', MovimentacaoInsumoDeleteView.as_view(), name='movimentacaoinsumo_delete'),

    # OUTROS
    path('movimentacoes/excel/', excel_movimentacoes, name='excel_movimentacoes'),
    path('registros/excel/', excel_registros, name='excel_registros'),
    ]
