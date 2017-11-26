from math import factorial

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return factorial(2*n) / (factorial(n + 1) * factorial(n))
        
