test = {
    "Topic_Name" : [
        {"Race": [
            {"White": "B02001002", "value": 8},
            {"Black": "B02001003", "value": 4},
            {"Native Indian": "B02001004", "value": 3},
            {"Asian": "B02001005", "value": 7},
            {"Native Hawaiian": "B02001006", "value": 6},
        ], "value": 9},
        {"Income": "B21002001", "value": 7},
        {"Education": "B15003002", "value":8},
        {"Poverty":"B17001002", "value": 8}
    ],
    "Count" : 5,
    "Type" : "Top"
}

lis1 =[]
length =len(test.get("Topic_Name"))
print("test----->", len(test.get("Topic_Name")))
for i in range(length):
    a = list(test.get("Topic_Name")[i].keys())[0]
    lis1.append(a)

print("lis1", lis1)
a = list(test.get("Topic_Name")[0].keys())[0]
b = list(test.get("Topic_Name")[1].keys())[0]
c = list(test.get("Topic_Name")[2].keys())[0]
d = list(test.get("Topic_Name")[3].keys())[0]
# e = list(test.get("Topic_Name")[4].keys())[0]

print("a------>:", a)
print("b------>:", b)
print("c------>:", c)
print("d------>:", d)
#print("e------>:", e)