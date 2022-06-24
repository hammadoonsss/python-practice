# Converting Decimal value to Binary
n=int(input("Enter decimal value: "))
l=[]

while(n!=0):
    a=int(n%2)
    l.append(a)
    n=int(n/2)
    
def reverse(l):
    new = l[::-1]
    return new

# print(l)
print(reverse(l))