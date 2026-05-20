# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            current = stack.pop()
            result.append(current.val)
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
        return result