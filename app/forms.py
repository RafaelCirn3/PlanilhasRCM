from django import forms

from .models import Servico, RegistroServico
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
