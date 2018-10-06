# function to get the difference of sum of square of n numbers and square of n numbers sum
def getdiff(number):
    squaresum = sumsquare = 0
    i = 1
    while i<= number:
        squaresum += i * i
        sumsquare += i
        i+=1
    sumsquare = sumsquare * sumsquare
    return (sumsquare - squaresum)

# Get the input
number = int(input("Enter the N Natural number:")

# Print the difference 
print("the Difference is ", getdiff(number))
