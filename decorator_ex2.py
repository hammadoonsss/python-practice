# ---Decorator Example 2---

def decorator_func(func):
    print("Inside Decorator")

    def inner(*args, **kargs):
        print("Inside inner function")
        print("Decorated the function")
        func()
    
    return inner


@decorator_func
def func_to():
    print("Inside actual function")

# func_to = decorator_func(func_to)

func_to()

