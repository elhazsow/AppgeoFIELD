from django.shortcuts import render
# from django.http import JsonResponse
from .models import ZonesProtgesDuSngal, NDVI
from django.core.serializers import serialize
# from djgeojson.serializers import Serializer as GeoJSONSerializer # type: ignore
# from django.contrib.gis.db.models.functions import Centroid
# from django.contrib.gis.geos import GEOSGeometry
# from django.contrib.gis.gdal import CoordTransform, SpatialReference


import numpy as np
# import math
import datetime
from django.db.models import Avg, Max
import json

from app import config
import ee
from app.earthengine import ee_get_image, get_map_tiles
import time

from shapely import to_geojson, geometry
from .bokey_utils import bokeh_chart





# Create your views here.

def view_test(request):
    sites=ZonesProtgesDuSngal.objects.all()
    sites_json = serialize('geojson', sites,
               fields=("id", "nom",'geom', 'superf_ha_field','arret_dec1','arret_dec2','arret_dec3','arret_dec4'))
    
    # serializer_ = Serializer(sites, many=True)
    # sites_json = (JsonResponse(serializer_.data, safe=True).content)
    last_year=NDVI.objects.aggregate(Max('date'))["date__max"].year - 1
    
    meanNdviLastYear = NDVI.objects.filter(date__gt = datetime.datetime(last_year,1,1)).values('id_k').annotate(avg_ndvi=Avg("ndvi"))
    
    
    context={}
    # context['sites']= sites
    
    context['sites_json']= sites_json
    return render(request, 'html\index.html', context)


def search_view(request):
    search_text=request.POST.get('search')
    results=ZonesProtgesDuSngal.objects.filter(nom__istartswith=search_text)
    context={}
    context['results']= results
    return render (request, 'html\search_result.html', context=context)


def site_view(request, id):
    
    
    site = ZonesProtgesDuSngal.objects.get(id=id)
    center = site.geom.centroid 

    pnt = center.transform(4326)
    
    context={}
    context['site'] = site
    context['centre'] = center

    return render(request,'html\site.html', context)


def chart_view(request,id):
   
    dates = np.array(NDVI.objects.filter(id_k=id).values_list('date',flat='true'))
    ndvi = np.array(NDVI.objects.filter(id_k=id).values_list('ndvi',flat='true'))
    zone =  ZonesProtgesDuSngal.objects.get(id=id)
    geom =  ZonesProtgesDuSngal.objects.get(id=id).geom.transform(4326, clone='true')
    bbox = geom.extent
    # convert to valid geojson
    
    geom_ = {"type": "FeatureCollection","features": [{"type": "Feature","properties": {},"geometry": json.loads(geom.json)}]}
    geom_=geom_['features'][0]['geometry']
    
    
    # bbox_= to_geojson(geom)
    # print(bbox_)
    

    # ee image tile
    """Request an image from Earth Engine and render it to a web page."""
    ee.Initialize(config.EE_CREDENTIALS)
    
    START_DATE = '2024-11-01'
    END_DATE= '2024-12-01'
    CLOUD_FILTER = 60
    CLD_PRB_THRESH = 40
    NIR_DRK_THRESH = 0.15
    CLD_PRJ_DIST = 2
    BUFFER = 100
    # AOI = ee.Geometry.Polygon([[-17.68,14.399], [-15.66, 14.399], [-15.66, 16.43],[-15.68, 16.43], [-17.68, 16.39]])
    AOI=ee.Geometry(geom_, opt_proj='EPSG:4326')
    
    palet_ndvi = [
    'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718',
    '74A901', '66A000', '529400', '3E8601', '207401', '056201',
    '004C00', '023B01', '012E01', '011D01', '011301']
    
    ndviParams = {'bands':['ndvi'],'min': 0.1, 'max': 1, 'palette':palet_ndvi} # paramètres de visualisation pour 'ndvi'
    
  
    
    image = ee.Image(ee_get_image(START_DATE , END_DATE, CLOUD_FILTER, CLD_PRB_THRESH, NIR_DRK_THRESH, CLD_PRJ_DIST, BUFFER, AOI))
    ndvi__ = get_map_tiles(image, 'ndvi', ndviParams)# extracting ndvi band
    gci = image.select('gci')  # extracting gci band
    ndwi = image.select('ndwi')  # extracting ndwi band
    
 
    
    # 'ndwi': {
    #     'mapid':ndwi['mapid'],
    #     'token':ndwi['token']
    # },
    
    # 'gci':{
    #     'mapid':gci['mapid'],
    #     'token':gci['token']
    # }
   
    
    # bokeh charts
    data = {'dates':dates, 'ndvi':ndvi}
    chart_ndvi = bokeh_chart(data, zone, "NDVI")
   
    
    context={}
    
    
    title = f"{zone.nom}"
    
    # cds= ColumDatasource(data=data)
    

    
    ###context
    props = {'nom':zone.nom,
           'superf_ha_field' : float(zone.superf_ha_field),
           'arret_dec1': zone.arret_dec1, 
        }
    props=json.dumps(props)
    context['script'] = chart_ndvi['script']
    context['div'] = chart_ndvi['div']
    context['bbox'] = [[bbox[1],bbox[0]],[bbox[3],bbox[2]]]
    context["props"] = props
    context["tiles"] = ndvi__['tiles']
    context["attr"] = str(ndvi__['attr'])
   

    



    return render(request,"html\_bokeh_chart.html", context)


