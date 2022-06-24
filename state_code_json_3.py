import json

def code_gen(state):
    try:
        json_file = "/home/hammdoon/Desktop/Real_Estate/static/state_codes.json"
        
        with open(json_file, 'r') as file:
            data = file.read()
            print("data---",type(data))
        state_code = json.loads(data)
        print("state_code---",type(state_code))
        
        
    except Exception as e:
        print("Error in JSON", e)
        
    state_list = []
    try:
        print("--state--0-", state)

        for i in state:
            if i in state_code:
                state_list.append(state_code[i])
            else:
                return None
        return state_list
    except Exception as e:
        print("Error as in GSD")

list1 = ["NY", "OH", "CO"]

print((code_gen(list1)))
