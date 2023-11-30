from django import forms
from .models import Aparelho, Emprestimo

class EmprestimoForm(forms.ModelForm):
    aparelho = forms.ModelChoiceField(queryset=Aparelho.objects.filter(status__nome='Disponível'))

    class Meta:
        model = Emprestimo
        fields = ['user', 'aparelho', 'dataEmprestimo', 'dataDevolucao']
