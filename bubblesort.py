# Method to do bubble sorting 
def bubblesort(NoofElem):
    i = 0 
    j = 0
    while i < NoofElem: 
        while j < NoofElem-i-1:
            if Iplist[j] > Iplist[j+1]:
                temp = Iplist[j]
                Iplist[j] = Iplist[j+1]
                Iplist[j+1] = temp
            j += 1
        i += 1
        j = 0

# List for holding the input values
Iplist = []

# Get the input from user
while True:
	try:
		Inp = int(input("Enter the numbers to sort one by one:"))
		Iplist.append(Inp)
	except:
		break
    
# Perform bubble sort
NoofElem = len(Iplist)
bubblesort(NoofElem)

# Print the results
print("printing lists in new line") 
print(*Iplist, sep = "\n") 
