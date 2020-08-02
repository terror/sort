def main():
    arr = [7, 4, 3, 2, 5, 1, 0, 4, 3, 1, 9, 1, 2]
    print(quick_sort(arr, 0, len(arr)-1))


def part(arr, lo, hi):
    piv, i = arr[hi], lo-1

    for j in range(lo, hi):
        if arr[j] < piv:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = part(arr, lo, hi)
        quick_sort(arr, lo, p-1)
        quick_sort(arr, p+1, hi)
    return arr


main()
