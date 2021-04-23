from sort import merge_sort


def test_merge_sort():
    arr = [4, 9, 0, 1, 3, 5, 2, 3, 9]
    assert merge_sort(arr) == sorted(arr)
