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
    print("=======", "546" in state_code)
    if state in state_code:
        return state_code[state]
    else:
        return None


print("---->>", get_state_dict("OH"))