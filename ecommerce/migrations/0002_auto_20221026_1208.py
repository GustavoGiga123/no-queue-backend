# Generated by Django 3.2.13 on 2022-10-26 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='numerohospedes',
            field=models.IntegerField(null=True, verbose_name='Número Hóspedes'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecommerce.hotel', verbose_name='Hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='estrelas',
            field=models.CharField(max_length=100, verbose_name='Estrelas'),
        ),
    ]
