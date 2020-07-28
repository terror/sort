from sort import merge_sort


def test_merge_sort():
    arr = [4, 9, 0, 1, 3, 5, 2, 3, 9]
    targ = [0, 1, 2, 3, 3, 4, 5, 9, 9]
    assert(merge_sort(arr) == targ)
