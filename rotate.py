def leftRotation(l, d):
    # left rotate array l by d positions
    # e.g. if a = [5, 1, 2, 3, 1] and d = 4
    for i in range(d):
        temp = l[i]
        for j in range(1, len(l)):
            l[j - 1] = l[j]
        l[j] = temp
    return l


a = [5, 1, 2, 3, 1]
print a
print(leftRotation(a, 3))
