from sort import counting_sort


def test_counting_sort():
    arr = [4, 5, 5, 7, 3, 2, 1, 0]
    targ = [0, 1, 2, 3, 4, 5, 5, 7]
    k = (max(arr)-min(arr))+1
    assert(counting_sort(arr, k) == targ)
