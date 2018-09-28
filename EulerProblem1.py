# Solution for Problem 1 of Project Euler

# Method to get the sum of the numbers between 1 and 1000 that are divisible by 3 and 5
def SumOfMultp():
	i = 1
	Tot = 0
	TotalNumber = 1000	
	while i <= TotalNumber:
		if (IsDivisible(i) == 1) 
			Tot += i
		i += 1

# Method to check if number is divisible by 3 or 5
def IsDivisible(i):
	if (i%3 == 0 or i%5 == 0):
		return 1
	else:
		return 0

print("The total sum of all the multiples of 3 or 5 below 1000", Tot)
