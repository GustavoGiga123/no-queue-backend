from django.db import models

  
class Hotel(models.Model):
  nome = models.CharField("Nome", max_length=100)
  endereco = models.CharField("Endereço", max_length=100)
  foto = models.ImageField(upload_to='filmes', max_length=255, null=True)
  estrelas = models.CharField("Estrelas", max_length=100)
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade")
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
  cpfourg = models.CharField("CPF ou RG", max_length=100)
  telefone = models.CharField("Telefone", max_length=100)
  email = models.EmailField()
  quarto = models.ForeignKey('Quarto',     on_delete=models.PROTECT, verbose_name="Quarto")
  def __str__(self):
    return f"N.º {self.id} - {self.email} - Hotel: {self.quarto}"
    
  

class Cidade(models.Model):
  nome = models.CharField("Nome", max_length=255)
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Cidade"
      verbose_name_plural = "Cidades"