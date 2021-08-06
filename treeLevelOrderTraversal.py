'''N-ary Tree-Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).'''

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        queue = deque([root])
        result = []
        while len(queue):
            level_result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_result.append(node.val)
                for child in node.children:
                   queue.append(child)
            result.append(level_result)
            
        return result
