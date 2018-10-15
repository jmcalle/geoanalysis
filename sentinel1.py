from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
#from datetime import date
import os
import logging

#connect to the API
#East Min (-81.173)   East max (-80.197)    , North Min (26.207)   North Max (27.063)

sentineluser = os.environ.get("SENTINEL_USER")
sentinelpwd = os.environ.get("SENTINEL_PWD")

logging.basicConfig(format='%(message)s', level='INFO')

api = SentinelAPI(sentineluser, sentinelpwd, 'https://scihub.copernicus.eu/dhus')
footprint = geojson_to_wkt(read_geojson("FCC_map.geojson"))
products = api.query(footprint,
                     date="[NOW-10DAY TO NOW]",
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 100))

#products = api.query(footprint, producttype='SLC', orbitdirection='ASCENDING')
api.download_all(products, max_attempts=10)

