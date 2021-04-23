from sort import insertion_sort


def test_insertion_sort():
    arr = [4, 5, 7, 3, 2, 1]
    assert insertion_sort(arr) == sorted(arr)
