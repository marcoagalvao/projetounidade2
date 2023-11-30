from django.shortcuts import render, redirect
from .models import Emprestimo, Aparelho, Status
from .forms import EmprestimoForm


def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'listar_emprestimos.html', {'emprestimos': emprestimos})

def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data['user']  # Obtenha o user_id do formulário
            emprestimo = form.save(commit=False)
            emprestimo.user = user_id
            emprestimo = form.save()
            #Mudar o status do aparelho solicitado
            aparelho = emprestimo.aparelho
            status_emprestado = Status.objects.get(nome='Emprestado')
            aparelho.status = status_emprestado
            aparelho.save()
    else:
        form = EmprestimoForm()

    return render(request, 'criar_emprestimo.html', {'form': form})