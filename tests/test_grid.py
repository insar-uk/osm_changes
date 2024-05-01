def test_grid():
    """The grid should be the height and width specified in the config file"""
    import osm_changes.config as config
    import osm_changes.grid as grid

    cfg = config.Config()
    grid = grid.Grid(cfg)

    assert len(grid.lat_points) == cfg.height
    assert len(grid.lon_points) == cfg.width
    assert len(grid.grid) == cfg.height * cfg.width

    # check the min/max values are in the grid
    assert cfg.min_lat in grid.lat_points
    assert cfg.max_lat in grid.lat_points
    assert cfg.min_lon in grid.lon_points
    assert cfg.max_lon in grid.lon_points
    
