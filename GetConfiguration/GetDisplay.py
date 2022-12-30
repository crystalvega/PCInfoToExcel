from winreg import *
import pyedid
from math import hypot

registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
def openRegistryA(dir):

    rawKeyA = OpenKey(registry, "SYSTEM\\CurrentControlSet\\Enum\\" + dir + "\\Device Parameters")

    try:
        i = 0
        while 1:
            name, value, type = EnumValue(rawKeyA, i)
            key = value
            i += 1


    except WindowsError:
        CloseKey(rawKeyA)
        return key      

def get(dir):
    edid_hex = openRegistryA(dir).hex()
    edid_result = ["", ""]
    edid = pyedid.parse_edid(edid_hex)
    edid_result[0] = edid.manufacturer + " " + edid.name
    edid_result[1] = round(round(hypot(edid.width, edid.height), 1)*0.393701, 1)
    json_str = str(edid)
    return edid_result