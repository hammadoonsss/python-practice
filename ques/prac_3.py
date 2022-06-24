# add a count value to all the existing values in the dictionary
# change value of keys in the dictinary with particular value

test = {
        'Hawaii': 2.6,
        'Washington': 2.6,
        'Alaska': 1.6,
        'California': 1.6,
        'New Jersey': 1.6
    }

count = 4
print("---------",test.values())

# test = test.values()+count
# print(test)

dic = {}
for i in test:
    print("i", i)
    #test[i] = test[i] + count
    test.update({i: count})
    
print(test)
    
