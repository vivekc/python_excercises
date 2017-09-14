numbers = [23, 64, 21, 22, 37, 56]  # [random.int() for i in range(10)]
numbers = [23, 3, 25, 15, 99, 9]


def buble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        nswaps = 0
        for i in range(n):
            j = i + 1
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                nswaps += 1
        print "%s %d" % (arr, nswaps)


print numbers
buble_sort(numbers)
