'''Given a 2D board and a word, find if the word exists in the grid.  The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        word_len_idx = len(word)-1
        
        def dfs(r, c, idx):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[idx]: return False
            if idx == word_len_idx:
                return True
            holding_cell = board[r][c]
            board[r][c]='-'
            res = dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1)  or dfs(r,c+1,idx+1)  or dfs(r,c-1,idx+1)
            board[r][c]=holding_cell
            return res

        # iterate board
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False             
