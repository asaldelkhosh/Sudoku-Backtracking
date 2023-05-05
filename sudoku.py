import numpy as np

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
    if i >= 0 and i <= n-1:
        pass
    else:
        i = input('Please enter a number between 0 to {} for i: '.format(n-1))
        i = int(i)

    if j >= 0 and j <= n-1:
        pass
    else:
        j = input('Please enter a number between 0 to {} for j: '.format(n-1)) 
        j = int(j)
        
    if value >= 1 and value <= n:
        pass
    else:
        value = input('Please enter a number between 1 to {} for value: '.format(n))
        value = int(value)

    arry[i, j] = value
    
    c = c - 1

    