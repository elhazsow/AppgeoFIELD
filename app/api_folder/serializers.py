from rest_framework_gis import serializers # type: ignore

from app.models import ZonesProtgesDuSngal ,ImageFile



class ZonesProtgesDuSngal_Serializer(
    serializers.GeoFeatureModelSerializer,
):
    class Meta:
        fields = [ "id","nom", 'superf_ha_field','arret_dec1','arret_dec2','arret_dec3','arret_dec4']
        geo_field = "geom"
        model = ZonesProtgesDuSngal
        


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = '__all__'