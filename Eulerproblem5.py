# Smallest number divisible by 1-20
def smallest():
    i = 21
    j = 1
    while True:
        while j <= 20:
            if i % j != 0:
                break
            if j == 20:
                return i
            j = j + 1
        i += 1
        j = 1

print("smallest is:", smallest())
