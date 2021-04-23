from sort import counting_sort


def test_counting_sort():
    arr = [4, 5, 5, 7, 3, 2, 1, 0]
    assert counting_sort(arr) == sorted(arr)
