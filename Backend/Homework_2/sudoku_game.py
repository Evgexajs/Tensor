def check(matrix, row, column, el):
    for x in range(0, 9):
        if matrix[x][column] == el and x != row:
            return False
    for y in range(0, 9):
        if matrix[row][y] == el and y != column:
            return False
    for x in range(0, 3):
        for y in range(0, 3):
            if (matrix[x + row - row % 3][y + column - column % 3] == el and (x + row - row % 3 != row and y + column - column % 3 != column)):
                return False
    return True

input_file = open('input.txt')
matrix = [[int(number) for number in line.split()] for line in input_file]
x = 0
y = 0
def solution_sudoku(matrix, x, y):
    if x == 8 and y == 9: return True
    if y == 9:
        x += 1
        y = 0
    if matrix[x][y] == 0:
        for el in range(1, 10):
            matrix[x][y] = el
            if check(matrix, x, y, el) and solution_sudoku(matrix, x, y + 1):
                return True
            else:
                matrix[x][y] = 0
    else:
        return solution_sudoku(matrix, x, y + 1)
    return False
 
if solution_sudoku(matrix, x, y):
    with open('output.txt', 'w') as output_file:
        for row in matrix:
            output_file.write(' '.join([str(a) for a in row]) + '\n')
else:
    print('Impossible')