dbt = [{'add': 123, 'value':6, 'token_id':"ABC"},
       {'add': 123, 'value':2, 'token_id':"ABC"},
       {'add': 456, 'value':4, 'token_id':"QWE"},
       {'add': 123, 'value':2, 'token_id':"ABC"},
       {'add': 345, 'value':6, 'token_id':"RTY"},
       {'add': 123, 'value':2, 'token_id':"ABC"},
       {'add': 456, 'value':6, 'token_id':"QWE"},
       {'add': 345, 'value':8, 'token_id':"RTY"} ]

sum = 0
db2 = {}
db3 = {}
print("---------------", type(dbt))
for ele in dbt:
    
    print('ele', ele)
    if ele['add'] == 123:
        sum += ele['value']
        db2['add'] = ele['add']
        db2['total_value'] = sum
        db2['token_id'] = ele['token_id']
        
        db3[ele['add']] = db2
        
        print('sum-------', sum)
    else:
        print('in else')

print('\nsum=', sum)
print('db2', db2)
print('db3', db3)


{'add':123, 'value':12}