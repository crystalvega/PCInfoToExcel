def get(ddrfromsheet, smbiosnumber):
    try:
        mt = smbiosnumber[0].SMBIOSMemoryType
        ddr = [(20, "DDR"), (21, "DDR2"), (22, "DDR2 FB-DIMM"), (24, "DDR3"), (26, "DDR4")]
        for memorytype in ddr:
            if memorytype[0] == mt:
                return memorytype[1]
    except Exception:
        return ddrfromsheet