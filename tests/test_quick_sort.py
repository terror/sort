from sort import quick_sort


def test_quick_sort():
    arr = [9, 4, 2, 4, 6, 7, 2, 3, 4, 5, 1, 1, 2]
    assert(quick_sort(arr, 0, len(arr)-1) == sorted(arr))
