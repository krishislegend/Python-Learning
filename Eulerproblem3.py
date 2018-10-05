# Function to get the primefactorial 
def primefactorial(number):
    factorial = []
    primestart = 2
    i = 2
    while i<= number:
        if (getprime(primestart)):
            while number % i == 0:
                factorial.append(i)
                number = number // i
            if number // i == 0:
                break
        i+=1
    return factorial
    
# Function to get the prime number list
def getprime(j):
    i = 1
    primeflag = 'Y'
    while i<= j:
        if i!= 1 and i!= j:
            if i %j == 0:
                return False
        i+= 1
    return True

# list to get the list of prome factors
fact = []

# Get the input number for which largest prime factor is required
number = int(input("Enter the number:"))

fact = primefactorial(number)
length = len(fact)
print("The largest prime factor is", fact[length-1])
