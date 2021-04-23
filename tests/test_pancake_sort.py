from sort import pancake_sort


def test_pancake_sort():
    arr = [4, 3, 7, 4, 2, 12, 45, 3, 0, 9, 4, 5]
    assert pancake_sort(arr, len(arr)) == sorted(arr)
