seats = [
            [True, True, True, True, True, True, True, True], 
            [True, True, True, True, True, True, True, True], 
            [True, True, True, True, True, True, True, True],
        ]

input_list = [4, 3,2, 1]
result_dict = {}

for ele in input_list:
    for row_index in range(0, len(seats)):
        row_value = row_index + 1
        if ele == 4:
            if all(seats[row_index][2:6]):
                for i in range(2, 6):
                    seats[row_index][i] = False
                    cha = chr(i+97)
                    if ele in result_dict:
                        result_dict[ele] += f"{row_value}{cha} "
                    else:
                        result_dict[ele] = f"{row_value}{cha} "
                break
            else:
                if all(seats[row_index][0:2]) and all(seats[row_index][6:8]):
                    seats[row_index][0] = False
                    seats[row_index][1] = False
                    seats[row_index][6] = False
                    seats[row_index][7] = False
                    result_dict[ele] = f"{row_value}a, {row_value}b, {row_value}g, {row_value}h"
                break
        elif ele == 3:
            print("in 3 ")
            if all(seats[row_index][2:5]):
                for i in range(2, 5):
                    seats[row_index][i] = False
                    cha = chr(i+97)
                    if ele in result_dict:
                        result_dict[ele] += f"{row_value}{cha} "
                    else:
                        result_dict[ele] = f"{row_value}{cha} "
                break
            else:
                continue
        elif ele == 2:
            pass
        elif ele == 1:
            for i in range(0, len(seats[row_index])):
                if seats[row_index][i] == True:
                    seats[row_index][i] = False
                    cha = chr(i+97)
                    if ele in result_dict:
                        result_dict[ele] += f"{row_value}{cha} "
                    else:
                        result_dict[ele] = f"{row_value}{cha} "
                    break
            break
        else:
            print("Sorry wrong Entry.....")
        
print("result_dict", result_dict)