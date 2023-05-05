import numpy as np

# Get n from user, n*n is the size of our matrix
n = input('n : ')
n = int(n)
np.zeros((n, n), dtype = int)

# Get c from user, c is the number of value that are in matrix
c = input('c : ')
c = int(c)

# Get values and the positions
while c > 0:
    i = input('i : ')
    if i >= 0 and i <= n-1:
        i = int(i)
        j = input('j : ')
    else:
        print('Please enter a number between 0 to {}'.formt(n-1))    
    if j >= 0 and j <= n-1:
        j = int(j)
        value = input('value : ')
    else:
        print('Please enter a number between 0 to {}'.formt(n-1))
    if value >= 1 and value <= n:        
        value = int(value)
    else:
        print('Please enter a number between 1 to {}'.formt(n))    
    c = c - 1

