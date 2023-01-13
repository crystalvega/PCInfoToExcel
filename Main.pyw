from GetConfiguration import GetConfiguration as gc
from OutputConfiguration import WorkBook as wb
from Path import path_is_file
import GUI, ZIP
from GUI import progress_bar
from command_runner.elevate import elevate
filename = "tablica1.xlsx"

def configuration(config):
    charters,disk = gc.get_char(config)
    wb.fileName = filename
    wb.allconfiguration = charters
    wb.diskconfiguration = disk
    wb.create()
    wb.wb, wb.sheet1, wb.sheet2 = wb.init()
    wb.rowinputall, wb.rowinputdisk = wb.checklastrecord()

def main():
    config = GUI.start("C:\\Program Files\\ConfigNKU\\confignku.txt")
    progress_bar
    ZIP.unpack("data.pkg","C:\Windows\Temp\dataofpack1")
    progress_bar.Value(10, progress_bar)
    configuration(config)
    progress_bar.Value(30, progress_bar)
    wb.configuration()
    progress_bar.Value(50, progress_bar)
    rowin, rowend = wb.configurationdisk()
    progress_bar.Value(80, progress_bar)
    wb.create_hyperlink(rowin, rowend)
    progress_bar.Value(100, progress_bar)
    wb.close()
    GUI.success()
    
if __name__ == "__main__":
    if path_is_file("~$" + filename) == False:
        elevate(main)
    else:
        GUI.Error()