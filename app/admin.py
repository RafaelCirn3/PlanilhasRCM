from django.contrib import admin
from .models import Insumo, MovimentacaoInsumo, Servico, RegistroServico, HistoricoUsuario

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_medida', 'escopo_minimo')
    search_fields = ('nome',)
    list_filter = ('unidade_medida',)

@admin.register(RegistroServico)
class RegistroServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'data', 'local_execucao', 'executado_por', 'realizado_periodo', 'percentual_realizado')
    search_fields = ('servico__nome', 'local_execucao')
    list_filter = ('data', 'servico')

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'quantidade_total')
    search_fields = ('nome',)
    list_filter = ('quantidade_total',)
    
@admin.register(MovimentacaoInsumo)
class MovimentacaoInsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'quantidade', 'finalidade', 'data', 'solicitado_por', 'registro_servico')
    search_fields = ('insumo__nome', 'finalidade')
    list_filter = ('data', 'insumo')

@admin.register(HistoricoUsuario)
class HistoricoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'data')
    search_fields = ('usuario__username', 'acao')
    list_filter = ('data',)