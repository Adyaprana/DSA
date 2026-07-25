class Solution(object):
    def missingNumber(self, nums):
        Expected = len(nums) * (len(nums)+1) //2
        Actual = sum(nums)
        num = Expected - Actual 
        return num
        