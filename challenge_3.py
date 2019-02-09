prime=[]
def prime_factor(i):
    for a in range (2,i):
        if(i%a == 0):
            break
    else:
        return True
        
def prime_divider(num1):
    for i in range(1000,int(num1/1000)):
        if num1%i == 0:
            if prime_factor(i):
                prime.append(i)
            else:
                continue
prime_divider(600851475143)
print(max(prime))
    
