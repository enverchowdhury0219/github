# day 23

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root: return None

#         root.left, root.right = root.right, root.left

#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root

# day 24

# max depth of a binary tree, using recursive DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))