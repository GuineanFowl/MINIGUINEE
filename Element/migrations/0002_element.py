# Generated by Django 5.0.6 on 2024-06-17 08:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Element', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('prix', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images_element')),
                ('est_vendu', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Elements', to='Element.categorie')),
                ('creer_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Elements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
