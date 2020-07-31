from heapq import heapify, heappop


def main():
    arr = [9, 3, 2, 6, 7, 3, 2, 0, 1, 2]
    print(heap_sort(arr))


def heap_sort(arr):
    n = len(arr)
    heapify(arr)
    ans = []
    for i in range(n):
        ans.append(heappop(arr))
    return ans


main()
