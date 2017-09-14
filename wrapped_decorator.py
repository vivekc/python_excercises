from pprint import pprint
from itertools import groupby
from functools import wraps


def logit(func):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        print(func.__name__ + " was called with arguments " + str(args))
        return func(*args, **kwargs)

    return my_wrapper


M = 50


@logit
def f(x):
    return (x * x + 1) % M


def main():
    l = range(50)
    items = list(enumerate(map(f, l)))
    sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
    pprint(sorted_items)
    # group by f(x)
    g = groupby(sorted_items, key=lambda x: x[1])
    keys = set()
    for key, value in g:
        keys.add(key)
        print key, list(value)
    print "distinct sums %s" % str(keys)


if __name__ == "__main__":
    main()
