def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def merge(arr, start, mid, end):
    if arr[mid - 1] < arr[mid]:
        return

    left = arr[start:mid]
    right = arr[mid:end]

    k = start
    i = 0
    j = 0

    while start + 1 < mid and mid + j < end:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if start + i < mid:
        arr[k:end] = left[i:]
    if mid + j < end:
        arr[k:end] = right[j:]


def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run), n - 1))

        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))
                merge(arr, start, mid, end)
            size *= 2

        return arr


a = ['b', 'a', 'd', 'f', 'g', 'h', 's', 'z', 'c']

print(timsort(a))