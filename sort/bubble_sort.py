def main():
    arr = [2, 5, 1, 0, 2, 4, 9]
    print(bubble_sort(arr))


def bubble_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        s = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                s = True
        if not s:
            break
    return arr


main()
