import operator

result = {
    'Maine': 0.2,
    'Vermont': 0.2,
    'West Virginia': 0.2,
    'New Hampshire': 0.2,
    'Wyoming': 0.2,
    'District of Columbia': 0.4,
    'Mississippi': 0.4,
    'Louisiana': 0.4,
    'Georgia': 0.4,
    'Maryland': 0.4,
    'Alaska': 1.6,
    'New Mexico': 0.6,
    'South Dakota': 0.6,
    'Oklahoma': 0.6,
    'Montana': 0.6,
    'Hawaii': 1.8,
    'California': 0.8,
    'New Jersey': 0.8,
    'Washington': 1.8,
    'New York': 0.8,
    'Utah': 1.0,
    'Nevada': 1.0
}

print("result:", type(result))

# Sort and Reverse the Dictionary using Lambda 
sorted_tuples_lambda = sorted(result.items(), key=lambda item: item[1], reverse=True)
print("sorted_tuples_lambda", sorted_tuples_lambda)

# Sort and Reverse the Dictionary using operator library
sorted_tuples = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
print("sorted_tuples: ", type(sorted_tuples))

if sorted_tuples_lambda == sorted_tuples:
    print("Same")
else:
    print("Not Same")

sorted_tuples_lambda= sorted_tuples_lambda[:5]
print("sorted_tuples_lambda: Top 5-----------", sorted_tuples_lambda)

sorted_tuples = sorted_tuples[:5]
print("sorted_tuples: Top 5----------", sorted_tuples)
