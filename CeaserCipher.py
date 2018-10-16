def breakcipher(listn):
    i = 1 
    j = 0 
    listnew = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    while i<= 26:
        for j in range(len(listn)):
            alphabet = listn[j]
            reverse = alpha[(alpha.find(alphabet)+i)%26]  
            listnew.append(reverse)
        print("Possible combinations", listnew)
        listnew.clear()
        i+=1
        j = 0
    
listn = list("kbslrpfknrbqbwmxpbqobebobru")
breakcipher(listn)
