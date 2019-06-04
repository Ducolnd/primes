from tqdm import tqdm


primes = []


for i in tqdm(range(1000000)):

    prime = True

    for x in range(i):
        if x == 0 or x == 1 or x == (i+1):
            continue

        if (i+1) % (x) == 0: #If remainer is 0 so it is divisable by something.

            prime = False
            break

    if prime:    
        primes.append((i+1))   #If it is not divisible by anything. 
print("done")

f = open("primes.txt", "a+")

for i in primes:
    f.write(str(i)+"\t")

f.close()

    
