from django.urls import path
from .views import (
    home, CustomLoginView,
    # SERVIÇO
    ServicoListView, ServicoDetailView, ServicoCreateView,
    ServicoUpdateView, ServicoDeleteView,

    # REGISTRO DE SERVIÇO
    RegistroServicoListView, RegistroServicoDetailView, RegistroServicoCreateView,
    RegistroServicoUpdateView, RegistroServicoDeleteView,

    # OUTROS
    excel_registros
)
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
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

    # OUTROS
    path('registros/excel/', excel_registros, name='excel_registros'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
