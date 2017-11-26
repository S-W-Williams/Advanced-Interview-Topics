# This is leetcode # 124

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        
        self.subMax = float("-inf")
        
        return max(self._helper(root), root.val, self.subMax)

        
    def _helper(self, root):
        if not root:
            return float("-inf")
        
        if not root.left and not root.right:
            return root.val
        
        leftSum = self._helper(root.left)
        rightSum = self._helper(root.right)
        
        curMax = max(root.val, root.val+leftSum, root.val+rightSum)
        
        if leftSum > curMax:
            self.subMax = max(self.subMax, leftSum)
        if rightSum > curMax:
            self.subMax = max(self.subMax, rightSum)
        if rightSum + leftSum + root.val > curMax:
            self.subMax = max(self.subMax, rightSum + leftSum + root.val)
            
        return curMax
