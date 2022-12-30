from GetConfiguration import GetConfiguration as gc
from OutputConfiguration import WorkBook as wb
from Path import resource_path_isfile
import GUI, ZIP
from command_runner.elevate import elevate

def configuration(config):
    charters,disk = gc.get_char(config)
    wb.fileName = "tablica.xlsx"
    wb.allconfiguration = charters
    wb.diskconfiguration = disk
    wb.create()
    wb.wb, wb.sheet1, wb.sheet2 = wb.init()
    wb.rowinputall, wb.rowinputdisk = wb.checklastrecord()

def main():
    config = GUI.start("C:\\Program Files\\ConfigNKU\\confignku.txt")
    ZIP.unpack("data.pkg","C:\Windows\Temp\dataofpack1")
    configuration(config)
    wb.configuration()
    rowin, rowend = wb.configurationdisk()
    wb.create_hyperlink(rowin, rowend)
    wb.close()
    GUI.success()
    
if __name__ == "__main__":
    if resource_path_isfile("~$tablica.xlsx") == False:
        elevate(main)
    else:
        GUI.Error()