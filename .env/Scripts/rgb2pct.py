#!C:\Users\Hp96\OneDrive\Bureau\geodjango\.env\Scripts\python.exe

import sys

from osgeo.gdal import UseExceptions, deprecation_warn

# import osgeo_utils.rgb2pct as a convenience to use as a script
from osgeo_utils.rgb2pct import *  # noqa
from osgeo_utils.rgb2pct import main

UseExceptions()

deprecation_warn("rgb2pct")
sys.exit(main(sys.argv))
