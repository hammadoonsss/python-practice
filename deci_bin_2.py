# Converting Decimal value to Binary (Using recursion)
l=int(input("Enter Decimal value:"))
a=[]
p = " "
def dec_bin(l):
    if (l == 0):
        return a
    temp = int(l%2)
    a.append(temp)
    l=int(l/2)
    return dec_bin(l)

def reverse(l):
    new = l[::-1]
    new_n = p.join(map(str, new))
    return new_n

print("Binary number: ", reverse(dec_bin(l)))