def main():
    arr = [0, 4, 2, 6, 8, 3, 1, 2, 9]
    print(stooge_sort(arr, 0, len(arr) - 1))


def stooge_sort(arr, l, h):
    if l >= h:
        return

    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)
        stooge_sort(arr, l, (h - t))
        stooge_sort(arr, l + t, (h))
        stooge_sort(arr, l, (h - t))

    return arr


main()
