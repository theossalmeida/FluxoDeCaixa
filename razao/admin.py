from django.contrib import admin
from .models import Categoria, Lancamento, Tipo


class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'nome','valor', 'categoria')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome', 'categoria')
    

admin.site.register(Tipo)
admin.site.register(Categoria)
admin.site.register(Lancamento, LancamentoAdmin)
