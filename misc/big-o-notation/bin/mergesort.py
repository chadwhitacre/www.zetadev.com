"""Mergesort implementation.

Definition from Wikipedia:

   1. Divide the unsorted list into two sublists of about half the size.

   2. Divide each of the two sublists recursively until we have list sizes of
      length 1, in which case the list itself is returned.

   3. Merge the two sublists back into one sorted list.

   [http://en.wikipedia.org/wiki/Mergesort]


Python uses a version of mergesort called timsort <wink>:

   http://svn.python.org/projects/python/trunk/Objects/listsort.txt


"""
import random

def data(i):
    """Generate a list (len i) of random ints.
    """
    m = i*100
    return [random.randint(0, m) for j in range(i)]



def merge(arr1, arr2):
    """Given two sorted lists, return a stably merged list.
    """
    merged = []
    val1 = val2 = None

    while arr1 or arr2:

        # Remove the next smallest values from each queue.
        # ================================================
        # Quit the loop when either queue goes empty. The remaining items on
        # the other queue will have to be pushed onto the new stack.

        if val1 is None:
            if arr1:
                val1 = arr1.pop(0)
            else:
                break
        if val2 is None:
            if arr2:
                val2 = arr2.pop(0)
            else:
                break


        # If we got two values, compare them.
        # ===================================
        # If we decide to push only one value to the new stack, then set that
        # variable to None to signal that it should be replenished.

        if val1 < val2:
            merged.append(val1)
            val1 = None
        elif val1 == val2:
            merged.extend([val1, val2])
            val1 = val2 = None
        else: # val2 < val1
            merged.append(val2)
            val2 = None


    # Push leftovers onto stack.
    # ==========================

    val, arr = (val1, arr1) if (val2 is None) else (val2, arr2)
    if val is not None:
        merged.append(val)
    merged.extend(arr)


    return merged


#print merge([636], [83, 314])
#raise SystemExit



def mergesort(arr):
    """Return a sorted copy of arr.
    """
    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    middle = len_arr / 2
    front = mergesort(arr[:middle])
    back = mergesort(arr[middle:])

    return merge(front, back)


if __name__ == '__main__':
    import sys
    foo = data(int(sys.argv[1] if len(sys.argv) > 1 else 10))
    #print foo
    sorted = sorted(foo)
    #print sorted
    #print foo
    mergesorted = mergesort(foo)
    #print mergesorted
    assert sorted == mergesorted
