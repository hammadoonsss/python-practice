# Array Manipulation : Approach 1
n=10
queries=[[1,5,3],[4,8,7],[6,9,1]]
x=0

# create a list of n's zeros
def create_lit(n):
    lit = [0]*n
    return lit

# adding values
ad_lit = create_lit(n)

# run queries
for i in queries:
    for j in range(i[x]-1, i[x+1]):
        ad_lit[j] += i[x+2]
        
print("AA_A_A:", ad_lit)
print("MAX_A_A:", max(ad_lit))


x = int(input("Enter parent list capacity: "))
y = int(input("Enter child list capacity: "))

parentlist = []
childlist = []
for i in range(x):
    for j in range(y):
        childlist.append(int(input()))
    parentlist.append(childlist)
    childlist=[]
    
print(parentlist)
