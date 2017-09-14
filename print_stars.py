nrows = 4
for i in range(1, nrows):
    k =0
    s = ""
    for space in range(1, nrows-i):
        s += " "
        i += 1
    while k != 2*i-1:
        s += "*"
        k += 1
    print s
