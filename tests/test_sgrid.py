from __future__ import (absolute_import, division, print_function)

import os
import types

import pysgrid
import numpy as np

from netCDF4 import Dataset
from shapely.geometry import MultiPolygon, Polygon

import gridgeo

data_path = os.path.join(os.path.dirname(__file__), 'data')

coawst_string = os.path.join(data_path, '00_dir_NYB05.nc')

grid = gridgeo.GridGeo(coawst_string)


def test_nc_from_string():
    assert isinstance(grid.nc, str)


def test_grid():
    assert isinstance(grid.grid, pysgrid.SGrid2D)


def test_mesh():
    assert grid.mesh == 'sgrid'


def test_raster():
    assert isinstance(grid.raster, np.ndarray)


def test_raster_ndim():
    assert grid.raster.ndim == 3


def test_outline():
    assert isinstance(grid.outline, Polygon)


def test_polygons():
    assert isinstance(grid.polygons, MultiPolygon)


def test_geo_interface():
    assert isinstance(grid.__geo_interface__, dict)


def test_polygons_generator():
    assert isinstance(grid._polygons_generator, types.GeneratorType)


def test_to_geojson():
    assert isinstance(grid.to_geojson(), dict)


def test_to_geojson_property():
    geojson = grid.to_geojson()

    properties = ['title', 'description', 'marker-size', 'marker-symbol',
                  'marker-color', 'stroke', 'stroke-opacity', 'stroke-width',
                  'fill', 'fill-opacity']
    for prop in properties:
        assert prop in geojson['properties'].keys()


def test_nc_from_object():
    nc = Dataset(coawst_string)
    grid = gridgeo.GridGeo(nc)
    assert isinstance(grid.nc, Dataset)
