def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i

        while j > 0 and arr[j-1] > current_value:
            arr[j] = arr[j-1]
            j = j-1
        
        arr[j] = current_value

music_count = [156, 141, 35, 94, 88, 61, 111]
insertion_sort(music_count)
print(music_count)