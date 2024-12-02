def In(x, list):
    for i in list:
        if i == x:
            return True
    return False

def seqSearch(x, list, pos=0):
    while pos < len(list):
        if list[pos] == x:
            return pos
        pos += 1
    return -1



print(In(0, [1,2,3]))
print(In(1, [1,2,3]))
print(seqSearch(0, [1,2,3]))
print(seqSearch(2, [1,2,3]))