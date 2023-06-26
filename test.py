from os import walk
from dataclasses import dataclass
import hashlib
import os
import sys

@dataclass
class Plugin:
    """Class for keeping track of an item in inventory."""
    name: str
    path: float
    _hash: str 
    size: int

def checkName(name, allowed):
    for a in allowed:
        if a in name:
            return True 
    return False

plugin_names = sys.argv[1:]
f = []
for (dirpath, dirnames, filenames) in walk("./plugins"):
    for name in filenames:
        
        if checkName(name, plugin_names):
            f.append(Plugin(name, dirpath, "", 0))

sha256_hash = hashlib.sha256()
for plugin in f:
    with open(plugin.path + "\\" +  plugin.name, "rb") as file: 
        for byte_block in iter(lambda: file.read(4096),b""):
            sha256_hash.update(byte_block)
        plugin.size = os.stat(plugin.path + "\\" +  plugin.name).st_size
        plugin._hash = sha256_hash.hexdigest()
        print(plugin)







