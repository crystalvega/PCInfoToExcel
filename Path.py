import os, sys
from pathlib import Path

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)
    
def path_is_file(path):
    return Path(path).is_file()