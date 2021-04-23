def main():
    arr = [4, 5, 9, 2, 9, 0, 3]
    print(selection_sort(arr))


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if arr[m] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


main()
