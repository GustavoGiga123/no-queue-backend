from django.contrib import admin

from.models import Hotel
from.models import Reserva
from.models import Cidade
from.models import Quarto
from.models import Usuario

admin.site.register(Hotel)
admin.site.register(Reserva)
admin.site.register(Cidade)
admin.site.register(Quarto)
admin.site.register(Usuario)
