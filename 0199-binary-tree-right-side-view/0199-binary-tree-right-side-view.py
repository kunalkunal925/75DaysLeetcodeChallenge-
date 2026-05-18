# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                current = queue.pop(0)
                
                if i == level_size - 1:
                    result.append(current.val)
                    
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
        return result