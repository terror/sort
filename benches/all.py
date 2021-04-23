import timeit
import random
from prettytable import PrettyTable
from sort import *

sorts = [
    ("Counting sort", counting_sort),
    ("Pigeonhole sort", pigeonhole_sort),
    ("Quick sort", quick_sort, 2),
    ("Merge sort", merge_sort),
    ("Heap sort", heap_sort),
    ("Pancake sort", pancake_sort, 1),
    ("Bubble sort", bubble_sort),
    ("Insertion sort", insertion_sort),
    ("Selection sort", selection_sort),
    ("Stooge sort", stooge_sort, 2),
]


def gen_arr(n):
    return [random.randint(1, 1000) for _ in range(n)]


def table():
    t = PrettyTable()
    t.field_names = ["Algorithm", "Time"]
    return t


def main():
    t = table()
    n = 1000  # choose whatever;

    for sort in sorts:
        name, algo, *rest = sort
        arr = gen_arr(n)
        start = timeit.default_timer()

        if len(rest):
            args = rest[0]
            algo(arr, 0, len(arr) - 1) if args == 2 else algo(arr, len(arr))
        else:
            algo(arr)

        t.add_row([name, "{:.4f}s".format(timeit.default_timer() - start)])

    print(t)


if __name__ == "__main__":
    main()
