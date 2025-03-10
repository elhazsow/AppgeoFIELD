# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class ZonesProtgesDuSngal(models.Model):
    geom = models.MultiPolygonField()  # This is a geometry field.
    nom = models.CharField(max_length=254, blank=True, null=True)
    zcode = models.BigIntegerField(blank=True, null=True)
    statut = models.CharField(max_length=254, blank=True, null=True)
    superf_ha_field = models.DecimalField(db_column='superf_ha_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    arret_dec1 = models.CharField(max_length=254, blank=True, null=True)
    arret_dec2 = models.CharField(max_length=254, blank=True, null=True)
    arret_dec3 = models.CharField(max_length=254, blank=True, null=True)
    arret_dec4 = models.CharField(max_length=254, blank=True, null=True)
    observ_1 = models.CharField(max_length=254, blank=True, null=True)
    observ_2 = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zones protégées du Sénégal'
