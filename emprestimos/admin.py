from django.contrib import admin
from .models import Status, Aparelho, Emprestimo

# Register your models here.
admin.site.register(Status)
admin.site.register(Aparelho)
admin.site.register(Emprestimo)