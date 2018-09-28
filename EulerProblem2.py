# Solution for Problem 2 of Project Euler

# Generate Fibonnaci Method
def generateFib():
    i = 1
    j = 2
    k = 2
    count = 0 
    while(i <= 4000000):
        k = j
        if (j % 2 == 0):
            count += j
        j += i
        i = k
    print("The sum of Fibonnaci even numbers upto 4 million is", count)

generateFib()
