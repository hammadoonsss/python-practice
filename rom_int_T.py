rom_num = input("Enter the Roman Value: ") 
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def convert_int(x):
    total=0
    count=0
    
    while(count < len(x)):
        s1=values[x[count]]
        print("s1====", s1)
        if (count + 1 < len(x)):
            s2=values[x[count+1]]
            print("s2=====", s2)
            if (s1 >= s2):
                total = total + s1
                count = count + 1
                print(" if inside->total:{}, count: {}".format(total, count))
            else:
                total = total - s1
                count = count + 1
                print(" else inside->total:{}, count: {}".format(total, count))
        else:
            total = total + s1
            count = count + 1
            print(" else outside->total:{}, count: {}".format(total, count))
    return total

print("Rom to Int:", convert_int(rom_num))
    