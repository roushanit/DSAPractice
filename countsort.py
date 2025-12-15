def countSort(array):  # input: array with values as non-negative integers
    n = len(array)
    if n == 0:
        return []

    max_value = max(array)
    count = [0] * (max_value + 1)

    # count frequency of each element
    for num in array:
        count[num] += 1

    # calculate prefix sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # build output array
    output = [0] * n
    for i in range(n - 1, -1, -1):
        a = array[i]
        b = count[a] - 1
        output[b] = a
        count[a] -= 1

    return output


print(countSort([3, 4, 2, 3, 4, 1, 4]))

