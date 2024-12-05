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

def halfSearch(x, list, min=0):
    max = len(list)
    while True:
        if len(list[min:max]) == 1:
            return -1
        index = (len(list[min:max]) // 2) + min
        if list[index] == x:
            return index
        elif list[index] < x:
            min = index
        elif list[index] > x:
            max = index

print(In(0, [1,2,3]))
print(In(1, [1,2,3]))
print(seqSearch(0, [1,2,3]))
print(seqSearch(2, [1,2,3]))  
print(halfSearch(0, [1,2,3,4]))
print(halfSearch(17, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))