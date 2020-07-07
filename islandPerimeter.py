def islandPerimeter(grid):
    
    if not grid: 
        return 0
    
    grid_width, grid_height = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(grid_width):
        for j in range(grid_height):

            if grid[i][j] == 1:    # found land
                perimeter += 4
                
                if (i>0 and grid[i-1][j] == 1):   # but found land is connected to land, so decrement
                    perimeter -= 2
                if (j>0 and grid[i][j-1] == 1):
                    perimeter -= 2
                    
    return perimeter

mat1, sol1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 16
print(islandPerimeter(mat1), "should equal", sol1)

mat2, sol2 = [[]], 0
print(mat2, islandPerimeter(mat2), "should equal", sol2)

mat3, sol3 = [[1,0]], 4
print(mat3, islandPerimeter(mat3), "should equal", sol3)

mat4, sol4 = [[1,1]], 6
print(mat4, islandPerimeter(mat4), 'should equal', sol4)
