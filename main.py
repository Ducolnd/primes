for i in range(1000):
    prime = True
    for x in range(i):
        if x == 0 or x == 1 or x == (i+1):
            continue
        #print("%s / %s" % ((i+1), x))
        if (i+1) % (x) == 0: #If remainer is 0 so it is divisable by something.
            #print("%s is not a prime number" % (1+i))
            prime = False
            break

    if prime:    
        print("%s is a prime number" % (1+i))   #If it is not divisible by anything. 
print("done")
    
