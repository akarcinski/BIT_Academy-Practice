def Next_prime(x):
    if x <= 1:
        return 2
    if x == 2:
        return 3
        
    if x % 2 == 0:
        i = x + 1
    else:
        i = x + 2

    while True:
        k = 3
        flag = True

        while k * k <= i:
            if i % k == 0:
                flag = False
                break
            k += 2
        if flag:
            return i
        i += 2
