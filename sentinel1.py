from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

#connect to the API

api = SentinelAPI('juanma.calle', '00002293', 'https://scihub.copernicus.eu/dhus')
footprint = geojson_to_wkt(read_geojson("map.geojson"))
products = api.query(footprint,
                     date=('20151219', date(2015, 12, 29)),
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 30))

#products = api.query(footprint, producttype='SLC', orbitdirection='ASCENDING')
api.download_all(products)

