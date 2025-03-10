import ee
import json

# src="https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless"



def ee_get_image(START_DATE , END_DATE, CLOUD_FILTER, CLD_PRB_THRESH, NIR_DRK_THRESH, CLD_PRJ_DIST, BUFFER, AOI):


    def get_s2_sr_cld_col(aoi, start_date, end_date):
    # Import and filter S2 SR.
        s2_sr_col = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
            .filterBounds(aoi)
            .filterDate(start_date, end_date)
            .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', CLOUD_FILTER)))

        # Import and filter s2cloudless.
        s2_cloudless_col = (ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
            .filterBounds(aoi)
            .filterDate(start_date, end_date))

        # Join the filtered s2cloudless collection to the SR collection by the 'system:index' property.
        return ee.ImageCollection(ee.Join.saveFirst('s2cloudless').apply(**{
            'primary': s2_sr_col,
            'secondary': s2_cloudless_col,
            'condition': ee.Filter.equals(**{
                'leftField': 'system:index',
                'rightField': 'system:index'
            })
        }))




    def add_cloud_bands(img):
        # Get s2cloudless image, subset the probability band.
        cld_prb = ee.Image(img.get('s2cloudless')).select('probability')

        # Condition s2cloudless by the probability threshold value.
        is_cloud = cld_prb.gt(CLD_PRB_THRESH).rename('clouds')

        # Add the cloud probability layer and cloud mask as image bands.
        return img.addBands(ee.Image([cld_prb, is_cloud]))


    def add_shadow_bands(img):
        # Identify water pixels from the SCL band.
        not_water = img.select('SCL').neq(6)

        # Identify dark NIR pixels that are not water (potential cloud shadow pixels).
        SR_BAND_SCALE = 1e4
        dark_pixels = img.select('B8').lt(NIR_DRK_THRESH*SR_BAND_SCALE).multiply(not_water).rename('dark_pixels')

        # Determine the direction to project cloud shadow from clouds (assumes UTM projection).
        shadow_azimuth = ee.Number(90).subtract(ee.Number(img.get('MEAN_SOLAR_AZIMUTH_ANGLE')))

        # Project shadows from clouds for the distance specified by the CLD_PRJ_DIST input.
        cld_proj = (img.select('clouds').directionalDistanceTransform(shadow_azimuth, CLD_PRJ_DIST*10)
            .reproject(**{'crs': img.select(0).projection(), 'scale': 100})
            .select('distance')
            .mask()
            .rename('cloud_transform'))

        # Identify the intersection of dark pixels with cloud shadow projection.
        shadows = cld_proj.multiply(dark_pixels).rename('shadows')

        # Add dark pixels, cloud projection, and identified shadows as image bands.
        return img.addBands(ee.Image([dark_pixels, cld_proj, shadows]))


    def add_cld_shdw_mask(img):
        # Add cloud component bands.
        img_cloud = add_cloud_bands(img)

        # Add cloud shadow component bands.
        img_cloud_shadow = add_shadow_bands(img_cloud)

        # Combine cloud and shadow mask, set cloud and shadow as value 1, else 0.
        is_cld_shdw = img_cloud_shadow.select('clouds').add(img_cloud_shadow.select('shadows')).gt(0)

        # Remove small cloud-shadow patches and dilate remaining pixels by BUFFER input.
        # 20 m scale is for speed, and assumes clouds don't require 10 m precision.
        is_cld_shdw = (is_cld_shdw.focalMin(2).focalMax(BUFFER*2/20)
            .reproject(**{'crs': img.select([0]).projection(), 'scale': 20})
            .rename('cloudmask'))

        # Add the final cloud-shadow mask to the image.
        return img_cloud_shadow.addBands(is_cld_shdw)



    def apply_cld_shdw_mask(img):
        # Subset the cloudmask band and invert it so clouds/shadow are 0, else 1.
        not_cld_shdw = img.select('cloudmask').Not()

        # Subset reflectance bands and update their masks, return the result.
        return img.select('B.*').updateMask(not_cld_shdw)




    s2_sr_cld_col = get_s2_sr_cld_col(AOI, START_DATE, END_DATE)

    s2_sr_median = (s2_sr_cld_col.map(add_cld_shdw_mask)
                                .map(apply_cld_shdw_mask)
                                .median()).clip(AOI)
    
    
    #calcul de NDVI :permer de détecter la végétation

    ndvi = s2_sr_median.normalizedDifference(['B8','B4']).rename('ndvi')

    s2_sr_median = s2_sr_median.addBands(ndvi); #//ajout de la bandes 'ndvi' à notre image composite
    # print(s2_sr_median);

    #// calcul de NDWI : permer de détecter l'eau

    ndwi = s2_sr_median.normalizedDifference(['B11','B8']).rename('ndwi')

    s2_sr_median = s2_sr_median.addBands(ndwi) #//ajout de la bandes 'ndvi' à notre image composite
    # print(s2)



    #calcul de GCI : presence of Chlorophyll

    def func_gci(image):
    
        gci = image.expression('b(8)/b(3)  -1 ').rename('gci')
        return image.addBands(gci)


    s2_sr_median = func_gci(s2_sr_median)
    return s2_sr_median



def get_map_tiles(image,bands,visParams):
    
    
    map_id_dict = image.select(f'{bands}').getMapId(visParams)
    
    
    tile = ee.data.getTileUrl(map_id_dict, 123,4567, 8)
    tiles = tile.replace("/tiles/8/123/4567", "/tiles/{z}/{x}/{y}")
    
    
    
    # tiles = map_id_dict['tile_fetcher'].url_format
    attr = 'Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>'
    
    return {'tiles': tiles, 'attr':attr}