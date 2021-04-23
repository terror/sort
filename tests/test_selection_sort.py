from sort import selection_sort


def test_selection_sort():
    arr = [4, 3, 9, 2, 8, 1, 2, 0, 2]
    assert selection_sort(arr) == sorted(arr)
