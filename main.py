import math

for i in range(100):
    for x in range(i):
        if (i+1) % (x+1) == 0:
            print("%s is not a prime number" % i)
            break
        
    
