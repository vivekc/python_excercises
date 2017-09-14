# List comprehensions are more compact and faster than an explicit for loop building a list.
# This is because calling .append() on a list causes the list object to
# grow (in chunks) to make space for new elements individually, while
# the list comprehension gathers all elements first before creating the
# list to fit the elements in one go

from timeit import timeit

some_iterable = range(10000)


def slower():
    result = []
    for elem in some_iterable:
        result.append(elem)
    return result


def faster():
    return [elem for elem in some_iterable]


if __name__ == "__main__":
    print timeit('f()', 'from __main__ import slower as f', number=10000)
    print timeit('f()', 'from __main__ import faster as f', number=10000)
