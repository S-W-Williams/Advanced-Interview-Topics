# This generates the next lexicographical perumation of a given list of numbers
# This is Leetcode #31

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i
                
        if k == -1:
            nums.reverse()
            return
        
        j = None
        for i in range(k+1, len(nums)):
            if nums[i] > nums[k]:
                j = i
        
        nums[k],nums[j] = nums[j],nums[k]
        
        i = len(nums) - 1
        j = k+1
        
        while j < i:
            nums[j],nums[i] = nums[i],nums[j]
            j += 1
            i -= 1
        return
