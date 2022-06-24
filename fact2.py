# Factorial: Resurcive 
def factorial(x):
    return 1 if(x==0 or x==1) else x * factorial(x-1)

num=5

print("fact",factorial(num))
    