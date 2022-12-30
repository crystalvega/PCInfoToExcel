import subprocess, shutil, os
from Path import resource_path
def gen(path, args, config):
    subprocess.call(path + " /stext " +args, shell=False)
    os.makedirs(resource_path('SMART') + "\\" + config[1], exist_ok=True)
    smartpath = resource_path('SMART') + "\\" + config[1] + "\\" + config[0] + ".txt"
    shutil.copyfile(args, smartpath)
    return "SMART\\" + config[1] + "\\" + config[0] + ".txt"
   
def status(path):
    statusret = []
    i = False
    next = False
    y = -1
    with open(path, 'r', encoding='UTF-16 LE') as f:
        for line in f:
            line = line.replace("\n", "")
            if next == True:
                statusret[y][0] = line.replace("Raw Value         : ","")
                next = False
            if line == "Description       : Model":
                i = True
                next = True
                y += 1
                statusret.append(["0","Ok"])
            if line == "Description       : General Information":
                i = False
            if i == True:
                if line.startswith("Status") and line != "Status            : Ok" and line != 'Status            : ' and line != "Status            : Unknown":
                    statusret[y][1] = line.replace("Status            : ", "")
    if len(statusret) == 0:
        statusret.append(["0","Not Found"])
    return statusret

def smart(path, searchwords, modelsize):
    smartret = []
    y = False
    disknumb = -1
    with open(path, 'r', encoding='UTF-16 LE') as f:
        for line in f:
            line = line.replace("\n", "")
            if y == True:
                if pastline == 'Description       : Model':
                    disknumb += 1
                    i = 0
                    while i < len(modelsize):
                        if line.replace("Raw Value         : ", "") == modelsize[i][0]:
                            smartret.append((disknumb, "Size", str(round(int(modelsize[i][1])/1000211184)) + " ГБ"))
                        i += 1
                smartret.append([disknumb,pastline.replace('Description       : ', ''),line.replace("Raw Value         : ", "")])
                y = not y
                
            if set(searchwords) & set(line.split(': ')) or line == 'Description       : Model':
                y = not y
                pastline = line
            
    if len(smartret) < 4:
        smartret2 = [[0,"Size","Not Found"],[0,"Model","Not Found"],[0,"Firmware Revision","Not Found"],[0,"Power-On Hours (POH)","Not Found"],[0,"Power Cycle Count","Not Found"]]
        return smartret2
    else:
        return smartret