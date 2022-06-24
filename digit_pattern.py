# digit pattern

def pattern(n):
    
    for i in n:
        print("|", end="")
        print("*" * int(i))
        

num="12421"
pattern(num)