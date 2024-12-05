def Merge(a, b):
    x, y = 0, 0
    out = []
    for i in range(0, len(a)+len(b)):
        if y == len(b):
            out.append(a[x])
            x += 1
        elif x == len(a):
            out.append(b[y])
            y += 1
        elif a[x] <= b[y]:
            out.append(a[x])
            x += 1
        elif a[x] > b[y]:
            out.append(b[y])
            y += 1
    return out

def mergeSort(x, min = 0, max = None):
    if max == None:
        max = len(x)
    if len(x) == 2:
        return Merge([x[0]], [x[1]])
    if len(x) == 1:
        return x
    half = len(x) // 2
    return Merge(mergeSort(x[min:half]), mergeSort(x[half:max]))

print(mergeSort([1 ,2, 3, 2, 4, 5, 33, 43, 1, 23, 4, 22, 7, 3]))
        