from sort import selection_sort


def test_selection_sort():
    arr = [4, 3, 9, 2, 8, 1, 2, 0, 2]
    targ = [0, 1, 2, 2, 2, 3, 4, 8, 9]
    assert(selection_sort(arr) == targ)
