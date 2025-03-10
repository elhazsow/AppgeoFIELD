#!C:\Users\Hp96\OneDrive\Bureau\geodjango\.env\Scripts\python.exe

import sys

from osgeo.gdal import UseExceptions, deprecation_warn

# import osgeo_utils.gdal_edit as a convenience to use as a script
from osgeo_utils.gdal_edit import *  # noqa
from osgeo_utils.gdal_edit import main

UseExceptions()

deprecation_warn("gdal_edit")
sys.exit(main(sys.argv))
