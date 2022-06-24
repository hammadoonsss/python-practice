# Prime numbers from 1 to N.

def isPrime(x):
    if (x==0 or x==1):
        return False
    
    for i in range(2, x):   
        if (x%i==0):
            return False
    return True
        
num = 37

for i in range(1, num+1):
    if(isPrime(i)):
        print("----",i, end="")