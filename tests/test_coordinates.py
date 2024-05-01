def test_coordinates():
    import osm_changes.coordinates as coordinates
    lat = 51.5074
    lon = -0.1278
    tile, pix = coordinates.latlon_to_tile(lat, lon, 16)
    # check correct tile is returned
    assert tile == (32744, 21792), f"Expected (32744, 21792) but got {tile}"
    # check that the pixel coordinates are within the expected range
    assert 0 <= pix[0] < 256, f"Expected 0 <= x < 256 but got {pix[0]}"

    lat = 53.463
    lon = -2.291
    # check correct tile is returned
    tile = coordinates.latlon_to_tile(lat, lon, 16)[0]
    assert tile == (32350, 21207), f"Expected (32350, 21207) but got {tile}"
