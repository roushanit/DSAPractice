def selectionSort(l):
    n = len(l)

    for a in range(0, n-1):
        s = a
        for b in range(a+1, n):
            if l[b] < l[s]:
                s = b

        l[a], l[s] = l[s], l[a]


l = [5, 3, 4, 1, 2]

print("Before Selection_sort:", l)

selectionSort(l)

print("After Selection_sort:", l)

