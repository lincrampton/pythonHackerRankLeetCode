'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.'''

def setZeroes(matrix):
    if not matrix or not matrix[0]: return matrix
        
    zero_rows, zero_cols = set(), set()
        
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
                print('here', i, j)
                    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i in zero_rows or j in zero_cols:
                print('here', i, j)
                matrix[i][j] = 0
                    
    return matrix

input1 = [[1,1,1],[1,0,1],[1,1,1]]
output1 = [[1,0,1],[0,0,0],[1,0,1]]
print(setZeroes(input1), 'should equal', output1)
