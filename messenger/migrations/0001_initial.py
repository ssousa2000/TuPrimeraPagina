# Generated by Django 4.2.20 on 2025-04-26 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
