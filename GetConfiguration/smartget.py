import subprocess
def gen(path, args):
    subprocess.call(path + " " +args, shell=False)
   
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
                if line.startswith("Status") and line != "Status            : Ok" and line != 'Status            : ':
                    statusret[y][1] = line.replace("Status            : ", "")
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
                            smartret.append((disknumb, "Size", str(int(modelsize[i][1])/1000211184) + " ГБ"))
                        i += 1
                smartret.append([disknumb,pastline.replace('Description       : ', ''),line.replace("Raw Value         : ", "")])
                y = not y
                
            if set(searchwords) & set(line.split(': ')) or line == 'Description       : Model':
                y = not y
                pastline = line
    return smartret
    