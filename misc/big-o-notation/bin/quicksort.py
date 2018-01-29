"""Quicksort implementation.

Definition per Wikipedia:

    1. Pick an element, called a pivot, from the list.

    2. Reorder the list so that all elements which are less than the pivot come
       before the pivot and so that all elements greater than the pivot come
       after it (equal values can go either way). After this partitioning, the
       pivot is in its final position. This is called the partition operation.

    3. Recursively sort the sub-list of lesser elements and the sub-list of
       greater elements.

    [http://en.wikipedia.org/wiki/Quicksort]


"""
import random

def data(i):
    """Generate a list (len i) of random ints.
    """
    m = i*100
    return [random.randint(0, m) for j in range(i)]


def quicksort(arr):
    """Return a sorted copy of arr.
    """
    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    pivot = random.randint(0, len_arr-1) # this is the dumb part
    # sorry, actually this is smart:
    # http://en.wikipedia.org/wiki/Quicksort#Randomized_quicksort_expected_complexity

    lesser = []
    pivot_val = arr.pop(pivot)
    greater = []

    len_arr = len(arr)
    for i in range(len_arr):
        val = arr.pop()
        if val <= pivot_val:
            lesser.append(val)
        elif val > pivot_val:
            greater.append(val)

    return quicksort(lesser) + [pivot_val] + quicksort(greater)


if __name__ == '__main__':
    import sys
    foo = data(int(sys.argv[1] if len(sys.argv) > 1 else 10))
    sorted = sorted(foo)
    quicksorted = quicksort(foo)
    assert sorted == quicksorted
