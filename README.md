# OS map change detector

A simple tool to compare changes in OS OpenData maps between two dates.

See the tiles and layers [here](https://os.openstreetmap.org/). This is where data is sourced currently.


For example, here is a binary imaging showing new buildings constructed between 201610 and 202310 in Swindon, UK according to the maps.
<!-- Example jpg: https://github.com/insar-uk/osm_changes/blob/main/example.jpg-->

![Example](https://raw.githubusercontent.com/insar-uk/osm_changes/main/example.jpg)

There are a few artefacts in the output... the next step is to use a 'bwareaopen' Python equivalent to remove small areas of noisyness mainly around labels.


## Configuration:

Configuration is handled using the config/config.json file. Options are:

``` json
{
    "config": "default",
    "output": "tiff",
    "output_dir": "./output",
    "zoom": 16,
    "min_latitude": 51.52,
    "max_latitude": 51.56,
    "min_longitude": -1.75,
    "max_longitude": -1.71,
    "height": 1000,
    "width": 1000,
    "layer1": "201610",
    "layer2": "202310",
    "initial_label": "Nothing",
    "final_label": "Building"
  }
```

### Options:
- output: The format of the output file.
    - 'tiff': EPSG:4326 (WGS84) - Output Geotiffs for use in GIS software (e.g. QGIS)
    - 'png': EPSG:3857 (WGS84 / Pseudo-Mercator) - Output PNGs for use with a WMS Tile server (e.g. QGIS Server)
- min/max_latitude/longitude: The WGS84 bounding box of the area to download. Be careful not to make the bounding area too big as this will take a long time to download and process!
- layer1/layer2: The OSM layer to download given as 'YYYYMM' where YYYY is the year and MM is the month. The layers are used to compare the changes between the two dates. The default is '201610' and '202310' which are the OS OpenData layers for October 2016 and March 2021.
- initial_label/final_label: The labels to use for the two layers. Currently only 'Nothing' and 'Building' colours have been added. It's straightforward to add more colours and labels in the detector.py file.

The other options haven't really been tested so please leave them as default.
- congig: just a name for the current config
- output_dir: the directory to save the output files
- zoom the zoom level used to download tiles
- height/width: the height and width of a grid used to find tiles to download. This is used to find the tiles to download and is not the size of the output file (s). The output file will be the same size as the downloaded tiles.

## Install:

Make sure you habitually run your python scripts in a virtual environment:

Windows:
```PowerShell
python -m venv venv
.\venv\Scripts\Activate
```

unix:
```bash
python3 -m venv venv
source venv/bin/activate
```

Then to install the package just:
```bash
pip install .
# use -e flag to install in editable mode
```

## Usage:

The main script loads config.json, finds and downloads the tiles from OSM, compares the tiles over the two layers, and saves the output (png or geotiff) to the output directory.

```bash
python -m osm_changes
```

## Testing and code coverage:

```bash
coverage run --source osm_changes --branch -m pytest
coverage report -m --format=markdown > coverage_report.md
```
