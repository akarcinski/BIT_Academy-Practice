from queue import Queue
def Prime_number(x):
    if x <= 1: 
        return False
    if x == 2:
        return True
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
