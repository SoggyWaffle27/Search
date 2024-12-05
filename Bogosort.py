import random as rand

def Shuffle(x):
    out = []
    for i in x:
        out.insert(rand.randint(0, len(x)), i)
    return out

def bogosort(x):
    c = 0
    while True:
        c += 1
        x = Shuffle(x)
        prev = x[0]
        a = True
        for i in x:
            if prev <= i:
                prev = i
            else:
                a = False
        if a == True:
            break
    return x, c

print(bogosort([2,34, 34, 123, 3]))