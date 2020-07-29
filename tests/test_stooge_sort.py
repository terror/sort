from sort import stooge_sort


def test_stooge_sort():
    arr = [4, 2, 9, 1, 8, 4, 7, 2]
    assert(stooge_sort(arr, 0, len(arr)-1) == sorted(arr))
