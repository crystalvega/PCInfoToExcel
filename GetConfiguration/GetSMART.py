import subprocess, shutil, os
def gen(path, args, config):
    subprocess.call(path + " /copyexit", shell=False)
    os.makedirs('SMART' + "\\" + config[1], exist_ok=True)
    smartpath = "SMART\\" + config[1] + "\\" + config[0] + ".txt"
    shutil.copyfile(args, smartpath)
    return smartpath
   
def status(path):
    statusret = []
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.replace("\n", "")
            if "           Model : " in line:
                modelline = line
            if "Health Status" in line:
                statusret.append((modelline, line.replace("   Health Status : ", "")))
    if len(statusret) == 0:
        statusret.append(["0","Not Found"])
    return statusret

def smart(path, searchwords):
    smartret = []
    b = False
    disknumb = 0
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            if " : " in line:
                line = line.replace("\n", "")
                for word in searchwords:
                    if word in line:
                        smartret.append((disknumb, word, line.split(" : ")[1]))
                if "Drive Letter" in line:
                    disknumb += 1
    if len(smartret) < 4:
        smartret2 = [[0,"Size","Not Found"],[0,"Model","Not Found"],[0,"Firmware Revision","Not Found"],[0,"Power-On Hours (POH)","Not Found"],[0,"Power Cycle Count","Not Found"]]
        return smartret2
    else:
        return smartret