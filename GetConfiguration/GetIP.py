from netifaces import AF_INET, ifaddresses, interfaces

def get_ip():
    ipadret = ''
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        for ipad in addresses:
            if ipad != '127.0.0.1' and ipad != 'No IP addr':
                if ipadret == '':
                    ipadret = ipad
                else:
                    ipadret = ipad + ', ' + ipadret
    return ipadret