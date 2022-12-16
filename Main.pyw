import zipfile as z
from GetConfiguration import get_configuration as gc
from OutputConfiguration import workbook as wb
from path import resource_path
import GUI

def main():
    config = GUI.start("C:\\Program Files\\ConfigNKU\\confignku.txt")
    zipFile = z.ZipFile(resource_path('pack1.zip'), 'r')
    zipFile.extractall('C:\Windows\Temp\dataofpack1')
    zipFile.close()
    charters, disk = gc.get_char(config)
    wb.create(charters, disk)
    wb.smart_cursor(charters)
    #wb.configuration(charters, disk)
    print(charters)
    print(disk)

if __name__ == "__main__":
    main()