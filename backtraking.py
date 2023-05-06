# Impoting math for caculating radical n
import math


# This function checks that a number that is going to assign is not in that row and column and box
def is_valid(grid, r, c, k, n):
    not_in_row = k not in grid[r]
    not_in_column = k not in [grid[i][c] for i in range(n)]
    rdn = int(math.sqrt(n))
    not_in_box = k not in [grid[i][j] for i in range(r//rdn*rdn, r//rdn*rdn+rdn) for j in range(c//rdn*rdn, c//rdn*rdn+rdn)]
    return not_in_row and not_in_column and not_in_box

# This function going to walk on the matrix and fill it with the right numbrs
# r is short for row, c is short for column and n is the size of the matrix, grid is our matrix
def solve(grid, r=0, c=0, n=9):
    if r == n:
        return True
        # if we were in the last row, we are done
    elif c == n:
        return solve(grid, r+1, 0, n)
        # if we were on the last column, we show go next row
    elif grid[r][c] != 0:
        return solve(grid, r, c+1, n)
        # if the entry was filled, then we go to the next column
        # if it wasnot filled we are going to find check with is_valid function and then assign a number
    else:
        for k in range(1, n+1):
            if is_valid(grid, r, c, k, n):
                grid[r][c] = k
                if solve(grid, r, c+1, n):
                    return True
                grid[r][c] = 0
        return False
