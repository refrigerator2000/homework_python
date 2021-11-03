import random

def names(z,x,c,v):
    r = 0
    while r < v:
        yield (random.choice(z) + random.choice(x) + random.choice(c))
        r = r + 1
for i in names(["Ivan", "Andrey", "Vika", "Alexey"],[".Yoda", ".Beta", ".Indev", ".Pop"],[".V", ".E", ".N", ".A"],10):
    print(i)

    
    