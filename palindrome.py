def palindrome(n):
    
    divisor=1
    while (n / divisor >=10):
        divisor*=10
    
    while (n != 0):
        
        leading = n // divisor
        trailing = n % 10
        
        if (leading != trailing):
            return False
        
        n = (n % divisor)//10
        
        divisor = divisor / 100
    
    return True

num = 1001

if (palindrome(num)):
    print("Palindrome")
else:
    print("NOT palindrome")