# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.L = L
        self.R = R
        self.sum = 0
        self.traverse_bst(root)
        return self.sum
    def traverse_bst(self,root):
        if root:
            self.traverse_bst(root.left)
            self.traverse_bst(root.right)
            if root.val >= self.L and root.val <= self.R:
                self.sum += root.val
        


