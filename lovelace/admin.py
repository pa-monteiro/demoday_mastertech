from django.contrib import admin

# Register your models here.
 
# Importa todos os modelos criados em models.py
from.models import Usuario, Parceiras, Votacao, Opiniao, TipoAtendimento

# Registrar os modelos para que fiquem visíveis na página de admin
admin.site.register(Usuario)
admin.site.register(Parceiras)
admin.site.register(Votacao)
admin.site.register(Opiniao)
admin.site.register(TipoAtendimento)