import random

class RandCores:
    
    def __init__(self):
        self.rgb = []
        self.cores = []
        
c = RandCores()

for i in range(6):
    c.cores.append(random.randint(1,15))
    if c.cores[i] == 10:
        c.cores[i] = "a"
    elif c.cores[i] == 11:
        c.cores[i] = "b"
    elif c.cores[i] == 12:
        c.cores[i] = "c"
    elif c.cores[i] == 13:
        c.cores[i] = "d"
    elif c.cores [i] == 14:
        c.cores[i] = "e"
    elif c.cores [i] == 15:
        c.cores[i] = "f"

hex = ''.join(map(str, c.cores))
c.rgb.append("#")
c.rgb.append(hex)
print(''.join(c.rgb))