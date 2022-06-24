# Here are some examples:
# 1. For array ["3", "-2"] should return "-2"
# 2. For array ["5", "5", "4", "2"] should return "4"
# 3. For array ["4", "4", "4"] should return "-1" (duplicates are not considered as the second max)
# 4. For [] (empty array) should return "-1".
# 5. For ["-214748364801","-214748364802"] should return "-214748364802".

def second_highest(arr):
    if len(arr) <= 0:
        return "-1"
    
    highest = arr[0]
    sec_highest = None

    for ele in arr[1:]:
        if ele > highest:
            sec_highest = highest
            highest = ele
            
        elif ele == highest:
            continue
        
        else:
            if sec_highest is None:
                sec_highest = ele
            elif ele > sec_highest:
                sec_highest = ele
    
    if sec_highest is None:
        return "-1"
    else:
        return str(sec_highest)            
        

if __name__ == "__main__":
    
    arr = list(map(int, input().strip().split(" ")))
    result = second_highest(arr)
    print("Second Highest is: ", result)
