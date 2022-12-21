from openpyxl import load_workbook

def format_cpu(cpu):
    i = 0
    wordsdelete = ['12th Gen Intel(R) Core(TM)', '11th Gen Intel(R) Core(TM)', '10th Gen Intel(R) Core(TM)']
    for word in wordsdelete:
        if word in cpu:
            cpu = cpu.replace(wordsdelete[i], "Intel Core")
    if " Mobile" in cpu:
        cpu = cpu.replace(" Mobile", "")
    return cpu


def get_cpu_info(cpu):
    cpu_info = ['']*6
    wb = load_workbook('C:/Windows/Temp/dataofpack1/cfg/db.xlsx')
    sheet = wb['CPU']
    cpu = format_cpu(cpu)
    i = 1
    ipspec = 0
    while i < 3519:
        if sheet.cell(row = i, column = 1).value == cpu:
            cpu_info[5] = i
            while ipspec < 5:
                cpu_info[ipspec] = sheet.cell(row = i, column = ipspec+1).value
                ipspec += 1
        i += 1
    return cpu_info

def get_cpu_upgrade(procinf):
    wb = load_workbook('C:/Windows/Temp/dataofpack1/cfg/db.xlsx')
    sheet = wb['CPU']
    i = 3519
    allcpus = 0
    cpusret = []
    while i != 1:
        if sheet.cell(row = i, column = 4).value == procinf[3] and sheet.cell(row = i, column = 2).value > procinf[1]:
            if allcpus == 0:
                allcpus = sheet.cell(row = i, column = 1).value
            else:
                lastcpu = sheet.cell(row = i, column = 1).value
                allcpus = allcpus + ', ' + lastcpu
        i -= 1
    cpusret = [allcpus, lastcpu]
    return cpusret