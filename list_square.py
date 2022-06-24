list1 = [1,2,3,4,5]

list2 = list(map(lambda a: a**2, list1))

print("first", list1, "---", len(list1))

print("Second", list2)

def sq_dict(x):
    sq = dict()
    
    for i in range(0, len(x)+1):    
        sq[i] = i**2
        
    print("sq--=>", sq)


sq_dict(list1)
