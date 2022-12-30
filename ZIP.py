import zipfile as z
from Path import resource_path
def unpack(name, dir):
    zipFile = z.ZipFile(resource_path(name), 'r')
    zipFile.extractall(dir)
    zipFile.close()