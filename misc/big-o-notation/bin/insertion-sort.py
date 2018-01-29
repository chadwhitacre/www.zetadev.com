"""Insertion sort implementation.

Definition per Wikipedia:

    In abstract terms, every iteration of an insertion sort removes an element
    from the input data, inserting it at the correct position in the already
    sorted list, until no elements are left in the input. The choice of which
    element to remove from the input is arbitrary and can be made using almost
    any choice algorithm.

    [http://en.wikipedia.org/wiki/Insertion_sort]


"""
import random

def data(i):
    """Generate a list (len i) of random ints.
    """
    m = i*100
    return [random.randint(0, m) for j in range(i)]


def insertion_sort(arr):
    """Return a sorted copy of arr.
    """

    sorted = []
    while arr:

        # Grab any old value.
        # ===================

        val = arr.pop(0)


        # Insert the value into the new list at the proper place.
        # =======================================================

        for i in range(len(sorted)):
            if sorted[i] > val:
                sorted.insert(i, val)
                val = None
                break
        if val is not None: # largest so far
            sorted.append(val)

    return sorted


if __name__ == '__main__':
    import sys
    foo = data(int(sys.argv[1] if len(sys.argv) > 1 else 10))
    _sorted = sorted(foo)
    sorted = insertion_sort(foo)
    assert sorted == _sorted
