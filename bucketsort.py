def bucketSort(array):
    n = len(array)
    if n == 0:
        return array

    # Create empty buckets
    buckets = [[] for _ in range(n)]

    # Part 1: Normalize and distribute into buckets
    max_val = max(array)
    for num in array:
        normalized = num / (max_val + 1)
        bucket_index = int(n * normalized)
        buckets[bucket_index].append(num)

    # Part 2: Sort each bucket using insertion sort (merged)
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1

            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1

            bucket[j + 1] = key

    # Part 3: Combine sorted buckets
    output = []
    for bucket in buckets:
        output.extend(bucket)

    return output
arr = [42, 32, 33, 52, 37, 47, 51, 1,10, 14, 5, 34, 3]

print("Before sort:", arr)
sorted_arr = bucketSort(arr)
print("After sort:", sorted_arr)

