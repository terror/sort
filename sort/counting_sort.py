def main():
    arr = [4, 3, 1, 2, 0]
    k = (max(arr)-min(arr))+1
    print(counting_sort(arr, k))


def counting_sort(arr, k):
    f = [0]*k

    for i in range(len(arr)):
        f[arr[i]] += 1

    for i in range(1, len(f)):
        f[i] = f[i-1]+f[i]

    ans = [0]*k
    for i in range(len(arr))[::-1]:
        ans[f[arr[i]]-1] = arr[i]
        f[arr[i]] -= 1
    return ans


main()
