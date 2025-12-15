def merge(l, s, m, e):
    i = s
    j = m + 1
    k = 0
    temp = [None] * (e - s + 1)

    # move i and j up until one of them is outside the line
    while i <= m and j <= e:
        if l[i] <= l[j]:
            temp[k] = l[i]
            i += 1
        else:
            temp[k] = l[j]
            j += 1
        k += 1

    # if i is still in the line
    while i <= m:
        temp[k] = l[i]
        i += 1
        k += 1

    # if j is still in the line
    while j <= e:
        temp[k] = l[j]
        j += 1
        k += 1

    # copy temp to original list
    k = 0
    for i in range(s, e + 1):
        l[i] = temp[k]
        k += 1


def mergeSort(l, s, e):
    if s >= e:
        return

    m = (s + e) // 2
    mergeSort(l, s, m)
    mergeSort(l, m + 1, e)
    merge(l, s, m, e)


def mergeSortAlgorithm(l):
    mergeSort(l, 0, len(l) - 1)


l = [4, 3, 1, 2, 5, 0]

print("Before Merge_sort:", l)
mergeSortAlgorithm(l)
print("After Merge_sort:", l)

