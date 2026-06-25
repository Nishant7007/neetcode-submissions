# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_node_validity(self, node, left, right):
        if(not node):
            return True
        if(node.val<=left or node.val>=right):
            return False
        return self.check_node_validity(node.left, left, node.val) and self.check_node_validity(node.right, node.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_node_validity(root, float('-inf'), float('inf'))