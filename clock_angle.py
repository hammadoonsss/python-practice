h=int(input("Enter hour: "))
m=int(input("Enter minutes: "))

def clock_func(h,m):
    if h==12:
        h=0
    clock_angle= abs((h*30 + m*0.5) - (m*6))
    return clock_angle

print("Clock Angle: ", clock_func(h,m))