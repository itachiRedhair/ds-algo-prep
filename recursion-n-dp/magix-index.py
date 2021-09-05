def find_magic_index(arr):

    def find_magix_index_recursive(arr, start, end):
        if end < start:
            return -1
        middle = start + end / 2

        if arr[middle] < middle:
            return find_magix_index_recursive(arr, middle+1, end)

        if arr[middle] > middle:
            return find_magix_index_recursive(arr, start, middle-1)

        return middle

    return find_magix_index_recursive(arr, 0, len(arr)-1)
