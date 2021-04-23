def main():
    arr = [4, 3, 1, 2, 0]
    print(counting_sort(arr))


def counting_sort(arr):
    m = min(arr); f = [0] * ((max(arr) - m) + 1)

    for i in range(len(arr)):
        f[arr[i] - m] += 1

    for i in range(1, len(f)):
        f[i] = f[i - 1] + f[i]

    ans = [0] * len(f)
    for i in range(len(arr))[::-1]:
        ans[f[arr[i] - m] - 1] = arr[i]
        f[arr[i] - m] -= 1
    return ans


main()
