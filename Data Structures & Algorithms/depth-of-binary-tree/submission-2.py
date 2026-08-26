# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        queue = [(root, 1)] if root else []
        max_depth = 0

        while queue :
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            queue += [(node.left, depth + 1)] if node.left else []
            queue += [(node.right, depth + 1)] if node.right else []
        return max_depth
