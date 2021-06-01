from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tecnologias)

#-Mostra os campos como tabela na aba admin
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome','slug','projlink')
    #Auto-completar o campo slug
    prepopulated_fields = {'slug':('nome',)}
                        