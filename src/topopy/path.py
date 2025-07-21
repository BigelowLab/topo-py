from pathlib import Path

def root_path(filename = "~/.topodata"):

    ```
    Get the topopy data path from a user specified file
    
    @param filename str the name the file to store the path as a single line of text
    @return string data path
    ```
    p = Path(filename)
    with p.open as file:
      line = file.readline()
    return(line)

def set_root_path(path = "/mnt/s1/projects/ecocast/coredata/bathy",
                  filename = "~/.topodata"):
    ```
    Set the topopy data path
    
    @param path the path that defines the location of topotools data
    @param filename the name the file to store the path as a single line of text
    @return None
    ```
    p = Path(filename)
    p.write_text(path)
    return(None)
    

def topo_path(*args, root = root_path()):
    
    ```
    Retrieve the topo path
    
    @param *args str file path segments to append to the root
    @param root str, the root directory
    @return str path specification (which may not exists)
    ```
  Path(root[1], args)
}