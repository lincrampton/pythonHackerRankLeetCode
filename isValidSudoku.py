'''Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.  A Sudoku board (partially filled) could be valid but is not necessarily solvable.  Only the filled cells need to be validated according to the mentioned rules.'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # do the rows
        for row in chain(board, zip(*board)):
            nums = [i for i in row if i != "."]
            if len(set(nums)) != len(nums): return False
            
        # do the sub-boxes
        for x, y in product([1,4,7],[1,4,7]):
            nums = [board[x+i][y+j] for i,j in product([-1,0,1],[-1,0,1])]
            nums = [i for i in nums if i != "."]
            if len(set(nums)) != len(nums): return False
            
        return True
