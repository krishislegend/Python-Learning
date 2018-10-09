# Function to get the nth prime number
def getnprime(number):
    i = 2
    j = 1
    position = 0
    while True:
        if (getprime(i)):
            position += 1
        if position == number:
            break
        i += 1
    return i

def getprime(j):
    loop = 1
    while loop <= j:
        if loop != 1 and loop != j:
            if j % loop == 0:
                return False
        loop += 1
    return True

# Get the input number for which largest prime factor is required
number = int(input("Enter the number:"))

print("The nth prime number is", getnprime(number))
