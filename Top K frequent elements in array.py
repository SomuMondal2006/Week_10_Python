# Top K frequent elements in array
# https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1



from collections import Counter

def topKFrequent(arr, k):
    freq = Counter(arr)

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))

    return [num for num, count in sorted_items[:k]]


arr1 = [3, 1, 4, 4, 5, 2, 6, 1]
k1 = 2
print(topKFrequent(arr1, k1))

arr2 = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k2 = 4
print(topKFrequent(arr2, k2))
