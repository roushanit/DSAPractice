def insertionSort(l):
    n = len(l)

    for i in range(1, n):
        key = l[i]
        j = i - 1

        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]   # shifting
            j -= 1

        l[j + 1] = key



l = [4, 3, 1, 2]

print("Before sort:", l)
insertionSort(l)
print("After sort:", l)

