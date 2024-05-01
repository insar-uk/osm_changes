import requests_mock
from osm_changes.config import Config
from osm_changes.downloader import Downloader


def test_get_tile_png():
    cfg = Config()
    cfg.output_dir = "/tmp"
    downloader = Downloader(cfg)

    with requests_mock.Mocker() as m:
        m.get(
            "https://tile.openstreetmap.org/17/65521/43969.png",
            content=b"some image content",
        )

        # Call the method we are testing
        result = downloader.get_tile_png(17, 65521, 43969)

        # Assert that the method returned the expected result
        assert result == b"some image content"
