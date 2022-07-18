import collections, functools, operator
test_list = [
                {'Puerto Rico': 0.0},
                {'Mississippi': 0.0},
                {'Louisiana': 0.0},
                {'New Mexico': 0.0},
                {'West Virginia': 1.0}
            ]

map_result =  map(collections.Counter, test_list)
print("map_result", map_result)

functools_result = functools.reduce(operator.add, map_result)
print("functools_result", functools_result)

dict_result = dict(functools_result)
print("dict_result", dict_result)


result = dict(functools.reduce(operator.add,
         map(collections.Counter, test_list)))

print("123------",result)