# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, maxi):
        if(node):
            if(node.val>=maxi):
                self.count+=1
            maxi = max(node.val, maxi)
            self.traverse(node.left, maxi)
            self.traverse(node.right, maxi)

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.traverse(root, -10**4-1)
        return self.count