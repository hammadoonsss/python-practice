# Factorial using lambda function
fact = lambda x : 1 if x<=1  else x * fact(x-1)

num=5
print(fact(num))