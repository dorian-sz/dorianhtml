
def osszeg(n):
    counter = 0
    for i in range(n + 1):
        counter += i
    return counter

print(osszeg(10))
