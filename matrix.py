R = int(input("Enter the n:")) 

  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(R):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 

# Print matrix
print("matrix: \n",matrix)

# For printing the matrix 
for i in range(R): 
    for j in range(R): 
        print(matrix[i][j], end = " ") 
    print()

# Adding diagonals
first_diagonal=0
second_diagonal=0

for i in range(0, R):
    first_diagonal += matrix[i][i]
    second_diagonal += matrix[i][R-1-i]
    
print('first_diagonal', first_diagonal)
print('second_diagonal', second_diagonal)

# Difference between diagonal
differ = first_diagonal - second_diagonal
differ_abs = abs(differ)
print("Differnce: ", differ_abs)


