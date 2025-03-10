from django.contrib.gis.db import models

# Create your models here.

class ZonesProtgesDuSngal(models.Model):
    geom = models.MultiPolygonField(srid=32628)  # This is a geometry field.
    nom = models.CharField(max_length=254, blank=True, null=True)
    zcode = models.BigIntegerField(blank=True, null=True)
    statut = models.CharField(max_length=254, blank=True, null=True)
    superf_ha_field = models.DecimalField(db_column='superf_ha_', max_digits = 13, decimal_places = 3, blank=True, null=True)  # Field renamed because it ended with '_'.
    arret_dec1 = models.CharField(max_length=254, blank=True, null=True)
    arret_dec2 = models.CharField(max_length=254, blank=True, null=True)
    arret_dec3 = models.CharField(max_length=254, blank=True, null=True)
    arret_dec4 = models.CharField(max_length=254, blank=True, null=True)
    observ_1 = models.CharField(max_length=254, blank=True, null=True)
    observ_2 = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        ordering = ["nom"]
        db_table = 'zones protégées du Sénégal'

    # Returns the string representation of the model.
    def __str__(self):
        return self.nom

class NDVI(models.Model):
    
    id_k = models.ForeignKey(ZonesProtgesDuSngal, verbose_name="clef secondaire", on_delete=models.CASCADE)
    date = models.DateField("date ", auto_now=False, auto_now_add=False)
    ndvi=models.FloatField("ndvi")
    
    # Returns the string representation of the model.
    def __str__(self):
        return f'{self.ndvi}'
    
class ImageFile(models.Model):
    Country_name = models.CharField(max_length=50, blank=False, null=True)
    image_file = models.FileField()
    index_type = models.TextField()
    
    
    def __str__(self): return self.Contry_name


