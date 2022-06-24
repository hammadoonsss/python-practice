# Factorial: Iterative
def factorial(x):
    if x<0:
        return 0
    elif x==0 or x==1:
        return 1
    else:
        fact=1
        while x>1:
            fact *=x
            x -= 1
        return fact
    
num=5
print("fact", factorial(num))