class Solution(object):
    def maxSubArray(self, nums):
        Current_Sum = 0
        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] > (Current_Sum + nums[i]):
                Current_Sum = nums[i]                    
            else:
                Current_Sum += nums[i]
            if ans < Current_Sum:
                ans = Current_Sum
        return ans