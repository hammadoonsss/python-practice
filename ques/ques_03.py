# Decorator 

def decorator(func):
    def inner(*args, **kwargs):
        print("test")
        result = func(*args, **kwargs)
        return result
    return inner

@decorator
def add_two(a,b):
    return a+b

print(add_two(a=10, b=30))
        