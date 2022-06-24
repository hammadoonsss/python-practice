list1 =  [1,8,2,5,6,3,7,4,9]
#output=[8,6,4,2,1,3,5,7,9]

list1.sort()

# print(list1)
for i in list1:
    if i%2==0:
        print("even", i)
        c=i
        list1.remove(i)
        list1.insert(0,c)
print("list1", list1)