from sort import pigeonhole_sort


def test_pigeonhole_sort():
    arr = [1232, 5, 23, 57, 65, 1]
    assert pigeonhole_sort(arr) == sorted(arr)
