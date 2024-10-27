def selection_sort(arr):
    size = len(arr)
    for pass_num in range(size):
        minimum_index = pass_num

        for i in range(pass_num + 1, size):
            if arr[i] < arr[minimum_index]:
                minimum_index = i
        
        temp = arr[pass_num]
        arr[pass_num] = arr[minimum_index]
        arr[minimum_index] = temp

music_count = [156, 141, 35, 94, 88, 61, 111]
selection_sort(music_count)

print(music_count)