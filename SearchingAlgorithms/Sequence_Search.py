#Sequence search

def sequential_search(arr, item):
    i = 0
    found = False
    while i < len(arr) and not found:
        if arr[i] == item:
            found = True
        else:
            i += 1
    return found

music_count = [156, 141, 35, 94, 88, 61, 111]
print(sequential_search(music_count, 88))