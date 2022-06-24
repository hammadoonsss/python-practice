# Check Prime or NOT Prime
def prime_number(num):
    
    flag=False
    
    if num>1:
        for i in range(2, num):
            if (num%i)==0:
                flag=True
                break
    
    if flag:
        print("Not prime")
    else:
        print("Prime")
        
prime_number(70)
            
        
    