#Generate Pythogret triplets
def pythogerantriplet():
    x = y = z = summation = 1     
    while x <= 500:
        while y <= 500:
            while z <= 500:
                if (x + y + z == 1000):
                    if (x*x + y*y) == z*z: 
                        summation = x*y*z                         
                z+=1
            y+=1
            z =1
        x+=1 
        y = 1 
        z = 1 
    
    return summation 
    
print("The triplets are", pythogerantriplet())

