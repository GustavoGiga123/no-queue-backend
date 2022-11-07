# Generated by Django 3.2.13 on 2022-11-03 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0005_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecommerce.cidade', verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário logado'),
        ),
    ]