class Solution(object):
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            new_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
            new_min = min(nums[i], nums[i] * current_max, nums[i] * current_min)
            current_max = new_max
            current_min = new_min
            answer = max(answer, current_max)

        return answer

