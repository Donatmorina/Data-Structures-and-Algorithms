#Binary search

def binary_search(arr, item, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if item == arr[mid]:
        return True
    elif item < arr[mid]:
        return binary_search(arr, item, low, mid-1)
    else:
        return binary_search(arr, item, mid+1, high)

music_count = [156, 141, 35, 94, 88, 61, 111]
music_count.sort()
size = len(music_count)
result = binary_search(music_count, 88, 0, size-1)
print(result)