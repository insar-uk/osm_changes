def test_config():
    import osm_changes.config as config

    cfg = config.Config()

    # Check default values have been defined
    assert "default.json" in cfg.filepath
    assert cfg.config == "default"
    # check defaults for zoom/lat/lon are in range
    assert 0 < cfg.zoom < 20
    assert -90 < cfg.min_lat < 90
    assert -90 < cfg.max_lat < 90
    assert -180 < cfg.min_lon < 180
    assert -180 < cfg.max_lon < 180
    assert cfg.output in ["json", "csv", "tiff"]
