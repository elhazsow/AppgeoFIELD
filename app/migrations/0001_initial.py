# Generated by Django 5.0.7 on 2024-08-12 18:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZonesProtgesDuSngal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('nom', models.CharField(blank=True, max_length=254, null=True)),
                ('zcode', models.BigIntegerField(blank=True, null=True)),
                ('statut', models.CharField(blank=True, max_length=254, null=True)),
                ('superf_ha_field', models.DecimalField(blank=True, db_column='superf_ha_', decimal_places=65535, max_digits=65535, null=True)),
                ('arret_dec1', models.CharField(blank=True, max_length=254, null=True)),
                ('arret_dec2', models.CharField(blank=True, max_length=254, null=True)),
                ('arret_dec3', models.CharField(blank=True, max_length=254, null=True)),
                ('arret_dec4', models.CharField(blank=True, max_length=254, null=True)),
                ('observ_1', models.CharField(blank=True, max_length=254, null=True)),
                ('observ_2', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'zones protégées du Sénégal',
                'managed': False,
            },
        ),
    ]
