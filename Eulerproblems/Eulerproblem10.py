import time
import math

# Function to get the primefactorial
def primesummation(number):
    # Mark the performance of the algorithm
    start = time.time()
    primestart = 2
    sumofprime = 0
    while primestart < number:
        if (getprime(primestart)):
            sumofprime = sumofprime + primestart
        primestart += 1
    end = time.time()
    print("time is", end-start)
    return sumofprime

# Function to get the prime number list
def getprime(j):
    i = 1
    # Looping the number till Square root reduces complexity to O(n * sqrt(n))
    while i <= math.sqrt(j):
        if i != 1 and i != j:
            if j % i == 0:
                return False
        i += 1
    return True


# Get the input number for which largest prime factor is required
number = int(input("Enter the number:"))
print("The sum of prime numbers upto is", primesummation(number))
