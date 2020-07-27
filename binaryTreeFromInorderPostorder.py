'''Given inorder and postorder traversal of a tree, construct the binary tree.


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
            if not inorder or not postorder:
                return None
            
            index_map = { v:x for x,v in enumerate(inorder)}
            return self.DFS(0, len(inorder)-1, inorder, collections.deque(postorder), index_map)

    def DFS(self, left, right, inorder, postorder, index_map):
            if left > right: 
                return None
        
            val = postorder.pop()
            root = TreeNode(val)
            root_node_loc = index_map[val]
        
            root.right = self.DFS(root_node_loc+1, right, inorder, postorder, index_map)
            root.left = self.DFS(left, root_node_loc-1, inorder, postorder, index_map)
            return root
