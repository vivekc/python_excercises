from functools import wraps


def memoize(func):
    """momoize func's return value in a dictionary"""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (tuple(args[0]), args[1])
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    return wrapper


@memoize
def left_rotation(l, d, **kwargs):
    """left rotate array l by d positions
    e.g. if a = [5, 1, 2, 3, 1] and d = 4"""
    for i in range(d):
        temp = l[i]
        for j in range(1, len(l)):
            l[j - 1] = l[j]
        l[j] = temp
    return l


if __name__ == "__main__":
    a = [
        [5, 1, 2, 3, 1, 5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1],
        [5, 1, 2, 3, 1, 5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1],
        [5, 1, 2, 3, 1, 5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1],
        [5, 1, 2, 3, 1, 5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1],
        [5, 1, 2, 3, 1, 5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1,5, 1, 2, 3, 1]
        ]
    for aa in a:
        print(left_rotation(aa, len(aa)))

