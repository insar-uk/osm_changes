# osm_os_adapter.py
"""
This module provides a class to interact with the OpenStreetMap API for Ordinance Survey Maps.

See also:
tests/test_osm_os_adapter.py

Available datasets are:
April 2010
November 2010
May 2011
November 2011
May 2012
November 2012
May 2013
November 2013
April 2014
October 2014
May 2015
November 2015
April 2016
OS OpenMap Local - October 2016
OS OpenMap Local - April 2017
OS OpenMap Local - October 2017
OS OpenMap Local - April 2018
OS OpenMap Local - May 2018
OS OpenMap Local - April 2019
OS OpenMap Local - April 2020
OS OpenMap Local - October 2020
OS OpenMap Local - April 2021
OS OpenMap Local - October 2021
OS OpenMap Local - April 2022
OS OpenMap Local - October 2022
OS OpenMap Local - April 2023
OS OpenMap Local - October 2023
"""

import requests
import os
import pyproj


def lat_lon_to_OSGB36(lat: float, lon: float) -> tuple[float, float]:
    """
    Convert latitude and longitude to OSGB36 format.
    :param lat: float
    :param lon: float
    :return: tuple[float, float]

    see:
    - https://www.ordnancesurvey.co.uk/docs/support/guide-coordinate-systems-great-britain.pdf
    - pyproj @ https://pyproj4.github.io/pyproj/stable/index.html
    """

    # create a transformer to convert lat/lon to OSGB36
    transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:27700", always_xy=True)
    # transform the lat/lon to OSGB36
    x, y = transformer.transform(lon, lat)
    return x, y


class OSMAdapter:

    base_urls = {
        "202310",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2023_10/",
        "202304",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2023_04/",
        "202210",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2022_10/",
        "202204",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2022_04/",
        "202110",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2021_10/",
        "202104",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2021_04/",
        "202005",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2020_05/",
        "202004",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2020_04/",
        "201910",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2019_10/",
        "201804",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2018_04/",
        "201710",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2017_10/",
        "201704",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2017_04/",
        "201610",
        "https://os.openstreetmap.org/layer/gb_os_om_local_2016_10/" "201604",
        "https://os.openstreetmap.org/layer/gb_os_sv_2016_04",
        "201511",
        "https://os.openstreetmap.org/layer/gb_os_sv_2015_11",
        "201505",
        "https://os.openstreetmap.org/layer/gb_os_sv_2015_05",
        "201411",
        "https://os.openstreetmap.org/layer/gb_os_sv_2014_11",
        "201404",
        "https://os.openstreetmap.org/layer/gb_os_sv_2014_04",
        "201311",
        "https://os.openstreetmap.org/layer/gb_os_sv_2013_11",
        "201305",
        "https://os.openstreetmap.org/layer/gb_os_sv_2013_05",
        "201211",
        "https://os.openstreetmap.org/layer/gb_os_sv_2012_11",
        "201205",
        "https://os.openstreetmap.org/layer/gb_os_sv_2012_05",
        "201111",
        "https://os.openstreetmap.org/layer/gb_os_sv_2011_11",
        "201105",
        "https://os.openstreetmap.org/layer/gb_os_sv_2011_05",
        "201011",
        "https://os.openstreetmap.org/layer/gb_os_sv_2010_11",
        "201004",
        "https://os.openstreetmap.org/layer/gb_os_sv_2010_04",
    }

    def __init__(self):
        self.tile_url = "https://tile.openstreetmap.org/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
        }

    def get_tile_png(self, zoom: int, x: int, y: int) -> bytes:
        # https://tile.openstreetmap.org/17/65521/43969.png
        url = f"{self.tile_url}{zoom}/{x}/{y}.png"
        response = requests.get(url, headers=self.headers)
        # check if the request was successful and bytes were returned
        response.raise_for_status()
        return response.content


def test_save_tile():
    adapter = OSMAdapter()
    bytes = adapter.get_tile_png(17, 65521, 43969)
    # save the image bytes to a file
    if bytes:
        current_save_dir = os.path.dirname(os.path.realpath(__file__))
        with open("tile.png", "wb") as f:
            print(f"Saving file in {current_save_dir}")
            f.write(bytes)


def test_lat_lon_to_OSGB36():
    # lat = 51.5074
    # lon = -0.1278
    # Burr Close:
    lat = 51.50566
    lon = -0.0692
    # expected x = 538890.105, y = 185655.228
    x, y = lat_lon_to_OSGB36(lat, lon)
    print(f"lat: {lat}, lon: {lon} -> x: {x}, y: {y}")


if __name__ == "__main__":
    test_lat_lon_to_OSGB36()
