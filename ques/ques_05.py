# Reverse a String

# First Method
def reverse_s(string):
    string = string[::-1]
    return string

s1= "HomeTown"
print("R@1", reverse_s(s1))

# Second Method

def reverse_two(s):
    st=""
    
    for i in s:
      st = i+st
    return st

s2="Company"

print("R@2",reverse_two(s2))