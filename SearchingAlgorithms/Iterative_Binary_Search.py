# Iterative binary search

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if arr[mid] == item:
            found = True
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return found

music_count = [156, 141, 35, 94, 88, 61, 111]
music_count.sort() # Binary search will not work if the list is not sorted.
result = binary_search(music_count, 88)
print(result)
