def main():
    arr = [1232, 5, 23, 57, 65, 1]
    print(pigeonhole_sort(arr))


def pigeonhole_sort(arr):
    Max = max(arr)
    Min = min(arr)
    size = Max - Min + 1

    holes = [0] * size

    for i in arr:
        holes[i - Min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + Min
            i += 1
    return arr


main()
