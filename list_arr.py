n =  int(input("Enter n:"))
arr = list(map(int, input("Enter values:").split()))[:n]

first=arr[0]
second=-101
for i in arr:
    if first < i:
        second=first
        first=i 
    elif second < i and i < first:
        second=i
   


print(second)    

# print("n", n)
# print("arr", arr)
