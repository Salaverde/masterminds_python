n = 2
x = 0
while True:
    for m in range(1,n):
        if (n % m) != 0 and m != 1 and m != n:
            x += 1
        if x == 0:
            print (n)
            n += 1
            break
    x = 0
