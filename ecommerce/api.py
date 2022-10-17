from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from ecommerce.models import Cidade
from ecommerce.models import Hotel
from ecommerce.models import Quarto
from ecommerce.models import Reserva


#### Cidades ########################################
class CidadeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cidade
    fields = ['id', 'nome']

class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Cidade.objects.all().order_by('nome')
  serializer_class = CidadeSerializer 
######################################################



  
#### Hotels ########################################
class HotelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hotel
    fields = ['id', 'nome', 'endereco','foto']

class HotelViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Hotel.objects.all().order_by('nome')
  serializer_class = HotelSerializer 
######################################################


#### Quartos ########################################
class QuartoSerializer(serializers.ModelSerializer):
  hotel = HotelSerializer()
  class Meta:
    model = Quarto
    fields = ['id', 'acomodacoes', 'hotel', 'numero']

class QuartoViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Quarto.objects.all().order_by('numero')
  serializer_class = QuartoSerializer 
######################################################
  #### Reservas ########################################
class ReservaSerializer(serializers.ModelSerializer):
  hotel = HotelSerializer()
  quarto = QuartoSerializer()
  class Meta:
    model = Reserva
    fields = ['id', 'datadeentrada', 'datadesaida', 'numerodehospedes', 'cpfourg', 'telefone', 'email', 'hotel', 'quarto']

class ReservaViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Reserva.objects.all().order_by('id')
  serializer_class = ReservaSerializer 
######################################################





# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cidades', CidadeViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'quartos', QuartoViewSet)
router.register(r'reservas', ReservaViewSet)
