result_dict = {
    'Honolulu County': 4,
    'Kauai County': 4,
    'Aleutians West Census Area': 4,
    'Santa Clara County': 4,
    'San Francisco County': 4,
    'Kinney County': 4,
    'Harding County': 4,
    'Wilkinson County': 4,
    'Blaine County': 4,
    'Loudoun County': 4,
    'King County': 4,
    'Kusilvak Census Area': 4,
    'Monroe County': 4,
    'Jefferson County': 4,
    'Sterling County': 4,
    'Loving County': 4,
    'Kalawao County': 4,
    'Morgan County': 4,
    'Falls Church city': 4,
    'Kenedy County': 4,
    'Storey County': 4,
    'Terrell County': 4,
    'Powhatan County': 4,
    'Elbert County': 4,
    'Doddridge County': 5
}

def check2(test_dict):
    res = True
    
    test_val = list(test_dict.values())[0]
    print(test_val)


    for ele in test_dict:
        if test_dict[ele] != test_val:
            res = False 
            break
    
    return res
    
print("Are all values similar in dictionary? : " + str(check2(result_dict)))

a = check2(result_dict)

if a:
    print("Yes")
else:
    print("No")
    