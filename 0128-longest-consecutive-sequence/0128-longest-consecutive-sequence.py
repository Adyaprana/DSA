class Solution(object):
    def longestConsecutive(self, nums):

        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        current_count = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current_count += 1
            else:
                current_count = 1
            if current_count > count:
                count = current_count
        return count
