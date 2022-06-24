n = int(input("Enter the value:"))
matrix = []

for i in range(0, n):
    matrix.append(list(map(int, input().strip().split())))

print('Matrix', matrix)

for m in matrix:
    print("\n",m)