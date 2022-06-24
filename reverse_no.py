# --- Reverse of a Number ---

# n=int(input("Enter number: "))
# rev=0

# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# print("The reverse of the number:",rev)

n=734
rev =0

while(n>0):
    digit=n%10
    rev = rev*10+digit
    n =n//10

print("rev:  ", rev)