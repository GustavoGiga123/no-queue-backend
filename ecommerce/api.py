from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from ecommerce.models import Cidade
from ecommerce.models import Hotel
from ecommerce.models import Quarto
from ecommerce.models import Reserva
from ecommerce.models import Usuario


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
  cidade = CidadeSerializer()
  class Meta:
    model = Hotel
    fields = ['id', 'nome', 'endereco','foto','valor', 'cidade']

class HotelViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Hotel.objects.all().order_by('nome')
  serializer_class = HotelSerializer 
  def get_queryset(self):

    """
    Filtra hotel por cidade 
    """
    queryset = Hotel.objects.all().order_by('cidade')
    query = {}

    cidade = self.request.query_params.get('cidade', None)
    if cidade is not None:
      query['cidade'] = cidade

    print(query)
    queryset = queryset.filter(**query)    
    return queryset
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
    fields = ['id', 'datadeentrada', 'datadesaida', 'numerodehospedes','nome', 'cpfourg', 'telefone', 'hotel', 'quarto']

class ReservaViewSet(mixins.CreateModelMixin,viewsets.ReadOnlyModelViewSet):
  queryset = Reserva.objects.all().order_by('id')
  serializer_class = ReservaSerializer 
######################################################

  #### API de autenticação ###############################
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone', 'cidade']

class CreateUsuarioSerializer(serializers.ModelSerializer):
    cidade: CidadeSerializer()
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone', 'cidade' ]

class CreateUsuarioViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = CreateUsuarioSerializer   
  queryset = Usuario.objects.all()
  def perform_create(self, serializer):
    serializer.save(user = self.request.user)   

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'password',
        ]
    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = UserRegistrationSerializer  

class LoginViewSet(ViewSet):
  @staticmethod
  def create(request: Request) -> Response:
      user = authenticate(
          username=request.data.get('username'),
          password=request.data.get('password'))

      if user is not None:
        login(request, user)
        return JsonResponse({"id": user.id, "username": user.username})
      else:
        return JsonResponse(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

class UsuarioDetailsViewSet(ViewSet):
  serializer_class = UsuarioSerializer
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    usuarios = Usuario.objects.filter(user = request.user)
    usuario = usuarios[0] if usuarios.exists() else None
    serializer = UsuarioSerializer(usuario, many=False)
    return Response(serializer.data)

class UserDetailsSerializer(serializers.ModelSerializer):
  class Meta:
      model = get_user_model()
      fields = ('id', 'username')

class UserDetailsViewSet(ViewSet):
  serializer_class = UserDetailsSerializer
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    serializer = UserDetailsSerializer(request.user, many=False)
    return Response(serializer.data)


class LogoutViewSet(ViewSet):
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    logout(request)
    content = {'logout': 1}
    return Response(content)  
                






# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cidades', CidadeViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'quartos', QuartoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'currentusuario', UsuarioDetailsViewSet, basename="Currentusuario")
