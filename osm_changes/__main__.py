import logging
from osm_changes.config import Config
from osm_changes.grid import Grid
from osm_changes.coordinates import Coordinate, latlon_to_tile
from osm_changes.downloader import Downloader
from osm_changes.detector import Detector


log = logging.getLogger(__name__)


def main():
    # load configuration
    cfg = Config()
    # create grid
    grid = Grid(cfg)

    # create a set of tiles
    tiles: set[Coordinate] = set()

    # for each point in the grid, find the tile
    for point in grid.grid:
        tile = latlon_to_tile(point[0], point[1], cfg.zoom)[0]
        tiles.add(tile)

    print(f"Number of tiles: {len(tiles)}")

    # if len(tiles) < 105:
    #     print(tiles)
    # else:
    #     print("Too many tiles to display")

    for layer in [cfg.layer1, cfg.layer2]:
        log.info(f"Downloading tiles for layer {layer}")
        downloader = Downloader(cfg)
        downloader.set_layer(layer)
        downloader.download_tiles(tiles)
        log.info("Layer download complete")

    log.info("Detecting changes in tiles")
    detector = Detector(cfg, overwrite=True)
    detector.detect_changes_in_tiles(tiles)
    log.info("Detection complete")


if __name__ == "__main__":
    main()
