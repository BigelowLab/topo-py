import xarray as xr

def read_topo(filename):
  """
  Read a topography file (as ncdf)
  @param filename one ncdf resource
  @return xarray
  """
  x = xr.open_dataset(filename)
  return(x)
 