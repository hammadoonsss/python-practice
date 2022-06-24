# Fibonnaci Series (with generator)

a = int(input("Enter Amount: "))

def fib(n):
    a, b=0, 1
    for _ in range(n):
        yield a 
        a, b = b, a+b
    
print("Fib:", list(fib(a)))