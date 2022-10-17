# Generated by Django 3.2.13 on 2022-10-10 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('foto', models.ImageField(max_length=255, null=True, upload_to='filmes')),
                ('estrelas', models.CharField(max_length=100, verbose_name='Nome')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.cidade', verbose_name='Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100, verbose_name='Número')),
                ('acomodacoes', models.IntegerField(verbose_name='Acomodação')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.hotel', verbose_name='Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datadeentrada', models.DateField(verbose_name='Data de entrada')),
                ('datadesaida', models.DateField(verbose_name='Data de saída')),
                ('numerodehospedes', models.IntegerField(verbose_name='Número de hóspedes')),
                ('cpfourg', models.CharField(max_length=100, verbose_name='CPF ou RG')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254)),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.quarto', verbose_name='Quarto')),
            ],
        ),
    ]