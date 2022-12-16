import subprocess

def get():
    proc = subprocess.Popen('wmic /node:localhost /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct Get DisplayName | findstr /V /B /C:displayName || echo No Antivirus installed', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode().replace("\r", "").replace("\n", "")