'''Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).  '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        top_down = []
        nodes = [root]

        while nodes:
            top_down.append([node.val for node in nodes])
            leaf_nodes =[]
            for node in nodes:
                if node.left:
                    leaf_nodes.append(node.left)
                if node.right:
                    leaf_nodes.append(node.right)
            nodes = leaf_nodes

        return top_down[::-1]

input1 = [3,9,20,null,null,15,7]
output1 = [ [15,7], [9,20], [3] ]
print(levelOrderBottom(input1),"=", output1)

