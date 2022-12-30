import wmi, win32print
from GetConfiguration import GetDisplay, GetSMART, GetCPUListForUpgrade, GetAntivirus, GetDDR
from GetConfiguration.GetIP import get_ip

def get_char(config):
    allconf = []
    diskconf = []
    smartwords = ['Model', 'Power-On Hours (POH)', 'Power Cycle Count', 'Firmware Revision', ]
    i = 1

    c = wmi.WMI()
    modelsize = []
    for model in c.Win32_Diskdrive():
        modelsize.append((model.Model, model.Size))
    smartfile = GetSMART.gen('C:\\Windows\\Temp\\dataofpack1\\tools\\DiskSmartView.exe', 'C:\\Windows\\Temp\\dataofpack1\\tools\\smart.txt', config)
    status = GetSMART.status('C:\\Windows\\Temp\\dataofpack1\\tools\\smart.txt')
    smart = GetSMART.smart('C:\\Windows\\Temp\\dataofpack1\\tools\\smart.txt', smartwords, modelsize)
    display = GetDisplay.get(c.Win32_DesktopMonitor()[0].pnpdeviceid)
    cpufromdb =  GetCPUListForUpgrade.get_cpu_info(c.Win32_Processor()[0].Name)
    cpusupgrade = GetCPUListForUpgrade.get_cpu_upgrade(cpufromdb)
    physicalmemory = c.Win32_PhysicalMemory()
    ip = get_ip()

    allconf.append(("Автозаполнение", "V"))
    allconf.append(("Кабинет", config[1]))
    allconf.append(("LAN", ip))
    allconf.append(("ФИО", config[0]))
    allconf.append(("Монитор", display[0]))
    allconf.append(("Диагональ",display[1]))
    allconf.append(("Тип принтера", config[2]))
    allconf.append(("Модель принтера", win32print.GetDefaultPrinter()))
    allconf.append(("ПК", config[3]))
    allconf.append(("Материнская плата",c.Win32_BaseBoard()[0].Manufacturer + " " + c.Win32_BaseBoard()[0].product))
    allconf.append(("Процессор",c.Win32_Processor()[0].Name))
    allconf.append(("Частота процессора",str(c.Win32_Processor()[0].MaxClockSpeed) + " МГц"))
    allconf.append(("Баллы Passmark", cpufromdb[1]))
    allconf.append(("Дата выпуска", cpufromdb[2]))
    allconf.append(("Тип ОЗУ", GetDDR.get(cpufromdb[4], physicalmemory)))
    for list in physicalmemory:
        allconf.append(("ОЗУ, " + str(i) + " Планка", str(round(int(list.capacity)/1073741824)) + " ГБ"))
        i += 1
    while i < 5:
        allconf.append(("ОЗУ, " + str(i) + " Планка", ""))
        i += 1
    allconf.append(("Сокет", cpufromdb[3]))
    for j in range(1, 5):
        if j <= len(status):
            allconf.append((["Диск " + str(j), status[j-1][0]]))
            allconf.append((["Состояние диска " + str(j), status[j-1][1]]))
        else:
            allconf.append((["Диск " + str(j), ""]))
            allconf.append((["Состояние диска " + str(j), ""]))

    allconf.append(("Операционная система", c.Win32_OperatingSystem()[0].name))
    allconf.append(("Антивирус", GetAntivirus.get()))
    allconf.append(("CPU Под замену", cpusupgrade[1]))
    allconf.append(("Все CPU под сокет", cpusupgrade[0]))
    
    diskconf.append(("Автозаполнение", "V"))
    diskconf.append(("Кабинет", config[1]))
    diskconf.append(("LAN", ip))
    diskconf.append(("ФИО", config[0]))
    i = 0
    ifs = 0
    while i <= smart[len(smart)-1][0] and i < 4:
        diskconf.append((("Диск", i+1),("Наименование", smart[ifs+1][2]), ("Прошивка", smart[ifs+2][2]), ("Размер", smart[ifs][2]), ("Время работы", smart[ifs+3][2]+" Часов"), ("Включён", smart[ifs+4][2]+" Раз"), ("Состояние", status[i][1]), ("S.M.A.R.T.",'=HYPERLINK("' + smartfile + '")')))
        i +=1
        ifs +=5

    return allconf, diskconf