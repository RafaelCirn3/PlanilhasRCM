from django import forms

from .models import Servico, RegistroServico, Insumo, MovimentacaoInsumo

# Formulário para Servico
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'unidade_medida', 'escopo_minimo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'unidade_medida': forms.TextInput(attrs={'class': 'form-control'}),
            'escopo_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Registro de Serviço
class RegistroServicoForm(forms.ModelForm):
    class Meta:
        model = RegistroServico
        fields = [
            'servico',
            'local_execucao',
            'realizado_periodo',
            'fotos',
            'descricao',
            'observacoes'
        ]
        widgets = {
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'local_execucao': forms.TextInput(attrs={'class': 'form-control'}),
            'realizado_periodo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Formulário para Insumo
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nome', 'descricao', 'quantidade_total']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'quantidade_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Movimentação de Insumo
class MovimentacaoInsumoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoInsumo
        fields = ['insumo', 'quantidade', 'finalidade', 'solicitado_por', 'registro_servico']
        widgets = {
            'insumo': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'finalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'solicitado_por': forms.Select(attrs={'class': 'form-control'}),
            'registro_servico': forms.Select(attrs={'class': 'form-control'}),
        }
