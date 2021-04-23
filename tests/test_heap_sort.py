from sort import heap_sort


def test_heap_sort():
    arr = [4, 5, 22, 6, 7, 9, 2, 3, 22, 0, 9, 1, 3, 44, 25, 4]
    assert sorted(arr) == heap_sort(arr)
