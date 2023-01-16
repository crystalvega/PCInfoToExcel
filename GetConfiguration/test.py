cpu = "Intel(R) Core(TM) i3 CPU         540  @ 3.07GHz"

wordsdeleteintel = ['12th Gen ','11th Gen ','10th Gen ', '(R)', '(TM)', "CPU "]
wordsdeleteamd = [' with Radeon Vega Graphics', " Mobile", " Processor", " Quad-Core Processor           ", "(tm)"]
for word in wordsdeleteintel:
    if word in cpu:
        cpu = cpu.replace(word, "")
        if "  @" in cpu:
            cpu = cpu.split('  @')[0]
        elif " @" in cpu:
            cpu = cpu.split(' @')[0]
for word in wordsdeleteamd:
    if word in cpu:
        cpu = cpu.replace(word, "")
if "         " in cpu:
    cpu = cpu.replace("         ", "-")
if "       M " in cpu:
    cpu = cpu.replace("       M ", "-")
    cpu = cpu+"M"
        
print(cpu)