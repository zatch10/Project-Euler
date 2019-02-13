i=3
prime=[2]
def prime_factor(i):
    for a in range (2,i):
        if(i%a == 0):
            break
    else:
        return True
        
while len(prime)<10001:
    if prime_factor(i):
        prime.append(i)
    i+=1

print(max(prime))

    
