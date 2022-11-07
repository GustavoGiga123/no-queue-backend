from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

  
class Hotel(models.Model):
  nome = models.CharField("Nome", max_length=100)
  valor = models.DecimalField(max_digits=5, decimal_places=2, null=True)
  endereco = models.CharField("Endereço", max_length=100)
  foto = models.ImageField(upload_to='filmes', max_length=255, null=True)
  estrelas = models.CharField("Estrelas", max_length=100)
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade")
  numerohospedes = models.IntegerField("Número Hóspedes",null=True)
#  cidade = models.CharField("Cidade", max_length=255,null=True,blank=True)
  def __str__(self):
      return self.nome

class Quarto(models.Model):
  numero = models.CharField("Número", max_length=100)
  acomodacoes = models.IntegerField("Acomodação")
  hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name="Hotel")
  def __str__(self):
      return f"{self.hotel} - Quarto: {self.numero}"
  

class Reserva(models.Model):
  hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name="Hotel",null=True)
  datadeentrada = models.DateField("Data de entrada")
  datadesaida = models.DateField("Data de saída")
  numerodehospedes = models.IntegerField("Número de hóspedes")
  nome = models.CharField("Nome", max_length=100, null=True)
  cpfourg = models.CharField("CPF ou RG", max_length=100)
  telefone = models.CharField("Telefone", max_length=100)
  quarto = models.ForeignKey('Quarto',     on_delete=models.PROTECT, verbose_name="Quarto")
  def __str__(self):
    return f"N.º {self.id} - {self.email} - Hotel: {self.quarto}"

class Usuario(models.Model):
  nome = models.CharField("Nome", max_length=255)
  email = models.CharField("E-mail", max_length=100)
  telefone = models.CharField("Telefone", max_length=100, null=True)
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade", null=True)
  user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário logado", null=True)
  cpf = models.CharField("CPF", max_length=100, null=True)

 


   
 
     
  

class Cidade(models.Model):
  nome = models.CharField("Nome", max_length=255)
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Cidade"
      verbose_name_plural = "Cidades"


  