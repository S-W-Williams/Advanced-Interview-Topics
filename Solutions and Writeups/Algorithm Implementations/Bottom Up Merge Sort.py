#So this is actually wrong... I need to debug and fix and update the notes when I have time

def inplaceMergeSort(a):
    if len(a) < 2:
        return a
    m = 1
    while m < (len(a) - 1) // 2:
        i = 0
        while i + m < len(a):
            j = i
            while j < i + m:
                if a[j] > a[i+m]:
                    a[j],a[i+m] = a[i+m],a[j]
                j += 1
            i += 2*m
        m *= 2
    i = m
    j = 0
    while i < len(a):
        if a[j] > a[i]:
            a[j],a[i] = a[i],a[j]
        j += 1
        if j == i:
            i += 1
    return 

if __name__ == "__main__":
    a = [9,6,2,12,11,9,3,7]
    assert inplaceMergeSort(a) == sorted(a)
