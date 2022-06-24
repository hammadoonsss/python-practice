def armstrong(x):
    number = str(x)
    
    n = len(number)
    output=0
    for i in number:
        output = output+int(i)**n
        print(output)
        
    if output == int(number):
        return True
    else:
        return False
    
num = 153
print("armstrong", armstrong(num))
    
        