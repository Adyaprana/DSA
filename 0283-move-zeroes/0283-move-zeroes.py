class Solution(object):
    def moveZeroes(self, nums):
        w = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[w] = nums[i]
                if i != w:
                    nums[i] = 0
                w += 1
        return nums