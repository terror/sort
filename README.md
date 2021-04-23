## <p align='center'>sort</p>
<p align='center'>
<img src="https://travis-ci.com/terror/Sorting-Algorithms.svg?branch=master"/>
</p>

<p align='center'>Sorting algorithm implementations in Python3!</p>

## Contents

[Counting sort](https://github.com/terror/sort/blob/master/sort/counting_sort.py)<br/>
[Quick sort](https://github.com/terror/sort/blob/master/sort/quick_sort.py)<br/>
[Merge sort](https://github.com/terror/sort/blob/master/sort/merge_sort.py)<br/>
[Heap sort](https://github.com/terror/sort/blob/master/sort/heap_sort.py)<br/>
[Bubble sort](https://github.com/terror/sort/blob/master/sort/bubble_sort.py)<br/>
[Insertion sort](https://github.com/terror/sort/blob/master/sort/insertion_sort.py)<br/>
[Selection sort](https://github.com/terror/st/blob/master/sort/selection_sort.py)<br/>
[Stooge sort](https://github.com/terror/sort/blob/master/sort/stooge_sort.py)<br/>
[Pigeonhole sort](https://github.com/terror/sort/blob/master/sort/pigeonhole_sort.py)<br/>
[Pancake sort](https://github.com/terror/sort/blob/master/sort/pancake_sort.py)


## Benchmarks

N = 100

```
+-----------------+-----------+
|    Algorithm    |    Time   |
+-----------------+-----------+
|  Counting sort  |  0.0006s  |
| Pigeonhole sort |  0.0001s  |
|    Quick sort   |  0.0001s  |
|    Merge sort   |  0.0002s  |
|    Heap sort    |  0.0000s  |
|   Pancake sort  |  0.0007s  |
|   Bubble sort   |  0.0007s  |
|  Insertion sort |  0.0004s  |
|  Selection sort |  0.0005s  |
|   Stooge sort   |  0.0695s  |
+-----------------+-----------+
```

N = 1000

```
+-----------------+-----------+
|    Algorithm    |    Time   |
+-----------------+-----------+
|  Counting sort  |  0.0424s  |
| Pigeonhole sort |  0.0003s  |
|    Quick sort   |  0.0016s  |
|    Merge sort   |  0.0034s  |
|    Heap sort    |  0.0003s  |
|   Pancake sort  |  0.0621s  |
|   Bubble sort   |  0.0779s  |
|  Insertion sort |  0.0490s  |
|  Selection sort |  0.0471s  |
|   Stooge sort   |  17.7174s |
+-----------------+-----------+
```

N = 2500

```
+-----------------+-----------+
|    Algorithm    |    Time   |
+-----------------+-----------+
|  Counting sort  |  0.2603s  |
| Pigeonhole sort |  0.0008s  |
|    Quick sort   |  0.0045s  |
|    Merge sort   |  0.0089s  |
|    Heap sort    |  0.0009s  |
|   Pancake sort  |  0.3859s  |
|   Bubble sort   |  0.5083s  |
|  Insertion sort |  0.3186s  |
|  Selection sort |  0.2812s  |
|   Stooge sort   | 513.7399s |
+-----------------+-----------+
```
