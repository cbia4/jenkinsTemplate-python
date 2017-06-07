class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here
        nums.sort()
        sum = 0
        
        for i in range(0,len(nums),2):
        	sum += min(nums[i],nums[i+1])
        	
        return sum

