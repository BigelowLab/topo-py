import os
import os.path as op
import glob

def root_path(filename = "~/.topodata"):
    
    """
    Get the topopy data path from a user specified file
    
    @param filename str the name the file to store the path as a single line of text
    @return string data path
    """
    p = op.expanduser(filename)
    with open(p) as file:
      line = file.readline()
    return(line)

def set_root_path(path = "/mnt/s1/projects/ecocast/coredata/bathy",
                  filename = "~/.topodata"):
    """
    Set the topopy data path
    
    @param path the path that defines the location of topotools data
    @param filename the name the file to store the path as a single line of text
    @return None
    """
    p = op.expanduser(filename)
    with open(p) as file:
      file.write(path + "\n")
    return(None)
    

def topo_path(*args, root = root_path()):
    
    """
    Retrieve the topo path
    
    @param *args str file path segments to append to the root
    @param root str, the root directory
    @return str path specification (which may not exists)
    """
    p = root
    for arg in args:
        p = op.join(p, arg)
    return(p)

def gebco_path(*args, root = topo_path("gebco")):
    
    """
    Retrieve the gebco path
    @param *args str file path segments to append to the root
    @param root str, the root directory
    @return str path specification (which may not exists)
    """
    p = topo_path(*args, root = root)
    return(p)
    
def etopo_path(*args, root = topo_path("etopo")):
    
    """
    Retrieve the etopo path
    @param *args str file path segments to append to the root
    @param root str, the root directory
    @return str path specification (which may not exists)
    """
    p = topo_path(*args, root = root)
    return(p)
    
    

def list_topo(path = topo_path(), full_names = True, pattern = '*'):
   """ 
   List contents a directory
   @param path str the path to the Gebco data
   @oaram full_names bool if True then return full names else base names
   @param pattern str the glob pattern for searching 
   @return string list of directory contents
   """
   ff = glob.glob(path + "/" + pattern)
   if not full_names:
     for i in range(len(ff)):
       ff[i] = op.basename(ff[i])
   return(ff)

def list_gebco(path = gebco_path(), full_names = True, pattern = '*.nc'):
   """ 
   List contents to the GEBCO directory
   @param path str the path to the GEBCO data
   @oaram full_names bool if True then return full names else base names
   @param pattern str the glob pattern for searching 
   @return string list of directory contents
   """
   ff = list_topo(path, full_names = full_names, pattern = pattern)
   return(ff)

def list_etopo(path = etopo_path(), full_names = True, pattern = '*.nc'):

   """ 
   List contents to the ETOPO directory
   @param path str the path to the ETOPO data
   @oaram full_names bool if True then return full names else base names
   @param pattern str the glob pattern for searching 
   @return string list of directory contents
   """
   ff = list_topo(path, full_names = full_names, pattern = pattern)
   return(ff)
