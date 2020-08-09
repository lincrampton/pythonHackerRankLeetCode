'''In a given grid, each cell can have one of three values: 0 (empty cell); 1 (fresh orange); 2 (rotten orange).  Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1.'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        Deck = collections.deque()
        
        M, N, Fresh = len(grid), len(grid[0]), 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    Fresh += 1
                if grid[i][j] == 2:
                    Deck.appendleft((i,j,0))
        
        Levels = 0
        while Deck:
            r, c, level = Deck.pop()

            for x, y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (0 <= x < M) and (0 <= y < N) and grid[x][y] == 1:
                    grid[x][y] = 2 
                    Fresh -= 1
                    Deck.appendleft((x,y, level+1))
                    if level+1 > Levels:
                        Levels = level+1   
        
        return -1 if Fresh>0 else Levels
