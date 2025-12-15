def bubbleSort(l):
    n = len(l)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            break

l = [4, 3, 1, 2, 7, 11, 0, 9, 5]

print("Before sort:", l)
bubbleSort(l)
print("After sort:", l)

