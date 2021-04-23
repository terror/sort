def main():
    arr = [4, 8, 2, 1, 0, 9, 5, 2]
    print(pancake_sort(arr, len(arr)))


def f(arr, i):
    s = 0
    while s < i:
        t = arr[s]
        arr[s], arr[i] = arr[i], t
        s += 1
        i -= 1


def pancake_sort(arr, n):
    curr = n
    while curr > 1:
        m = arr[0:curr].index(max(arr[0:curr]))
        if m != curr - 1:
            f(arr, m)
            f(arr, curr - 1)
        curr -= 1
    return arr


main()
