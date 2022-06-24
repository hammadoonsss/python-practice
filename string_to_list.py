# Converting a string into list
# without using in-built function.
lit1 = 'a b c d'

lit2 = []

for i in lit1:
    if i == ' ' or i == ',':
        pass
    else:
        lit2 += [i]
        
print(lit2)
