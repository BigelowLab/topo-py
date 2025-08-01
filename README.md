# topo-py
Access locally stored topography data from GEBCO and ETOPO using python.




topotools
================

Coding tools for working with local copies of [ETOPO data](https://www.ncei.noaa.gov/products/etopo-global-relief-model) and [GEBCO data](https://www.gebco.net/data_and_products/gridded_bathymetry_data/#global).

This package is intended to mirror [R package topotools](https://github.com/BigelowLab/topotools).   For an overview see that package's [README](https://github.com/BigelowLab/topotools.md).

### ETOPO Citation

    NOAA National Centers for Environmental Information. 2022: ETOPO 2022 15 Arc-Second Global Relief Model. NOAA National Centers for Environmental Information. DOI: 10.25921/fd45-gt74. Accessed 2023-03-17.

### GEBCO Citation

    GEBCO Compilation Group (2022) GEBCO_2022 Grid (doi:10.5285/e0f0bb80-ab44-2739-e053-6c86abc0289c) Accessed 2023-03-17.
    GEBCO Compilation Group (2024) GEBCO 2024 Grid (doi:10.5285/1c44ce99-0a0d-5f4f-e063-7086abc0ea0f) Accessed 2024-07-17.
    

## Requirements

-  [Python v3.12+](https://www.python.org)
-  [xarray](https://xarray.dev/)

## Installation


## Usage

Establish the data path which should contain an `etopo` and a `gebco` subdirectory.  Each of those should contain one or more NetCDF files downloaded form the source above.

```
import topopy

set_root_path(path = "/mnt/s1/projects/ecocast/coredata/bathy")
```

Listing contents of the data directories.
```
list_topo()
# ['/mnt/s1/projects/ecocast/coredata/bathy/gebco', '/mnt/s1/projects/ecocast/coredata/bathy/etopo']

list_gebco()
# ['/mnt/s1/projects/ecocast/coredata/bathy/gebco/GEBCO_2022.nc', '/mnt/s1/projects/ecocast/coredata/bathy/gebco/GEBCO_2024.nc']

list_gebco(full_names = False)
# ['GEBCO_2022.nc', 'GEBCO_2024.nc']
```

Reading a file.
```
read_topo(list_gebco()[1])
# <xarray.Dataset> Size: 7GB
# Dimensions:    (lon: 86400, lat: 43200)
# Coordinates:
#   * lon        (lon) float64 691kB -180.0 -180.0 -180.0 ... 180.0 180.0 180.0
#   * lat        (lat) float64 346kB -90.0 -89.99 -89.99 ... 89.99 89.99 90.0
# Data variables:
#     crs        |S1 1B ...
#     elevation  (lat, lon) int16 7GB ...
# Attributes: (12/36)
#     title:                           The GEBCO_2024 Grid - a continuous terra...
#     summary:                         The GEBCO_2024 Grid is a continuous, glo...
#     keywords:                        BATHYMETRY/SEAFLOOR TOPOGRAPHY, DIGITAL ...
#     Conventions:                     CF-1.6, ACDD-1.3
#     id:                              DOI: 10.5285/1c44ce99-0a0d-5f4f-e063-708...
#     naming_authority:                https://dx.doi.org
#     ...                              ...
#     geospatial_vertical_units:       meters
#     geospatial_vertical_resolution:  1.0
#     geospatial_vertical_positive:    up
#     identifier_product_doi:          DOI: 10.5285/1c44ce99-0a0d-5f4f-e063-708...
#     references:                      DOI: 10.5285/1c44ce99-0a0d-5f4f-e063-708...
#     node_offset:                     1.0
```