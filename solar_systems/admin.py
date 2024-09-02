from django.contrib import admin
from .models import PanelSolar, Inversor, Bateria, SistemaFotovoltaico, Usuario, ControladorDeCarga

# Register your models here.

admin.site.register(PanelSolar)
admin.site.register(Inversor)
admin.site.register(Bateria)
admin.site.register(SistemaFotovoltaico)
admin.site.register(Usuario)
admin.site.register(ControladorDeCarga)
