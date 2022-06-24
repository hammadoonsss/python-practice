# Sum of value based on particular key in a dictionary 
l = [{'a': 1, 'b': 2},{'a': 6, 'b': 6},{'a': 4, 'b': 3}]

def su(l):
    li=[]
    for i in l:
        li.append(i['a'])
    print(li)
    return sum(li)

print(su(l))
