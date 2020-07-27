from sort import pigeonhole_sort


def test_pigeonhole_sort():
    arr = [1232, 5, 23, 57, 65, 1]
    targ = [1, 5, 23, 57, 65, 1232]
    assert(pigeonhole_sort(arr) == targ)
