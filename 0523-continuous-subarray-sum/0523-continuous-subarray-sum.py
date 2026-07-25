class Solution(object):
    def checkSubarraySum(self, nums, k):
        Running_Prefix = 0
        HashMap = {0: -1}
        for i in range(len(nums)):
            Running_Prefix += nums[i]
            remainder = Running_Prefix % k
            if remainder in HashMap:
                diff = i - HashMap[remainder]
                if diff >= 2:
                    return True
            else:
                HashMap[remainder] = i
        return False


