from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_emprestimos, name='listar_emprestimos'),
    path('criar/', views.criar_emprestimo, name='criar_emprestimo')
] 