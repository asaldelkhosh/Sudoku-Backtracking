import numpy as np
from backtraking import solve

# Get n from user, n*n is the size of our matrix
n = input('n : ')
n = int(n)

# Make a n*n arry with zeros
arry = np.zeros((n, n), dtype = int)

# Get c from user, c is the number of value that are in matrix
c = input('c : ')
c = int(c)

# Get values and the positions and changing them in arry
while c > 0:
    i = input('i : ')
    i = int(i)
    j = input('j : ')
    j = int(j)

    value = input('value : ')
    value = int(value)

    arry[i, j] = value
    
    c = c - 1

# Calling solve function from backtraking,py
if solve(arry, n=n) == True:
    print(*arry,sep='\n')
else: 
    print('Unsolvable CSP!')
 