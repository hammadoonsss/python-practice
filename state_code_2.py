def get_state_dict(state):
    state_code = {
        "FL" : "050|04000US12",
        "MA" : "050|04000US25",
        "NJ" : "050|04000US34",
        "NY" : "050|04000US36",
        "OH" : "050|04000US39",
    }
    print("state", state)
    print("state_code", state_code)
    state_list = []
    for i in state:
        print("---", i)
        if i in state_code:
            state_list.append(state_code[i])
        else:
            return None
    return state_list

print("---->>", get_state_dict(["OH", "NJ", "FL"]))