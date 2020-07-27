from sort import bubble_sort


def test_bubble_sort():
    arr = [2, 3, 1, 8, 4, 5, 0]
    targ = [0, 1, 2, 3, 4, 5, 8]
    assert(bubble_sort(arr) == targ)
