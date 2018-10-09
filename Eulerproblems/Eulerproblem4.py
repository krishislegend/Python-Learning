# Method to get the Palindrome number
def palindrome():
    i = 100
    j = 100
    palindrome = []
    
    # Loop from 100 to 999 for both 3 digit numbers
    while i <= 999:
        while j <= 999:
            res = str(i * j)
            rev = res[::-1]
            if res == rev:
                if not palindrome:
                    palindrome.append(res)
                else:
                    num1 = i * j 
                    num2 = int(palindrome[0])
                    if num1 > num2:
                        palindrome.pop(0)
                        palindrome.append(num1)
            j += 1
        j = 100
        i += 1
    return palindrome

print("The palindrome list is ", palindrome())
