class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in seen:
                return [seen[find],i]
            else:
                seen[nums[i]] = i
        