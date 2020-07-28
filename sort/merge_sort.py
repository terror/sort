def main():
    arr = [4, 5, 0, 1, 2, 4, 9, 8, 7]
    print(merge_sort(arr))


def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        l, r = arr[:mid], arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k], i = l[i], i+1
            else:
                arr[k], j = r[j], j+1
            k += 1

        while i < len(l):
            arr[k], k, i = l[i], k+1, i+1

        while j < len(r):
            arr[k], k, j = r[j], k+1, j+1

        return arr


main()
