class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        running_sum = 0
        for i in range(len(nums)):
            running_sum += (nums[i])
            runningSum.append(running_sum)
        return runningSum

        