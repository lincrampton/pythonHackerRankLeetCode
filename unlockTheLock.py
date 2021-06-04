'''You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
    
        WHEELS = 4   # number of wheels we can rotate on the lock
        LEGAL_MOVES = [-1, 1]
        IMPOSSIBLE = -1  # can never get to this point
        ROOT = '0000'   # starting point 
    
        deads = set(deadends)  # positions that make the process stop
        if ROOT in deads:    return -1     # easy exit
        
        def neighbors(node):
            for w in range(WHEELS):
                n = int(node[w])
                for m in LEGAL_MOVES:
                    r = (n + m) % 10
                    yield node[:w] + str(r) + node[w+1:]
                    
        deads = set(deadends)
        visited = {'0000'}
        queue = collections.deque([('0000', 0)])
        
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth 
            if node in deads: continue       
            for nachbarn in neighbors(node):     
                if nachbarn not in visited:
                    visited.add(nachbarn)          
                    queue.append((nachbarn, depth+1))          
                                 
        return IMPOSSIBLE
