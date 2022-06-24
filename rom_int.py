number = input("enter the roman_number:")
a = {'I': 1, 'V': 5, 'X': 10,'L':50, 'C':100, 'D':500, 'M':1000}
#n = "MDI"
count=0
for i in number:
    count = count + a[i]
print(count)
