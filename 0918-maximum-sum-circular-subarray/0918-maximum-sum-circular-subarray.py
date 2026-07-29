class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = nums[0]

        min_current = nums[0]
        min_subarr = nums[0]

        max_current = nums[0]
        max_subarr = nums[0]
        for i in range(1, len(nums)):
            total_sum += nums[i]
            if nums[i] < (min_current + nums[i]):
                min_current = nums[i]
            else:
                min_current += nums[i]
            if min_current < min_subarr:
                min_subarr = min_current

            if nums[i] > (max_current + nums[i]):
                max_current = nums[i]
            else:
                max_current += nums[i]
            if max_current > max_subarr:
                max_subarr = max_current

        if min_subarr == total_sum:
            return max_subarr
        return max(max_subarr, total_sum - min_subarr)




# class Solution(object):
#     def maxSubarraySumCircular(self, nums):
#         current_sum = nums[0]
#         total_sum = nums[0]
#         min_subarr = nums[0]
#         max_subarr = nums[0]
#         for i in range(1, len(nums)):
#             total_sum += nums[i]
#             if nums[i] < (current_sum + nums[i]):
#                 current_sum = nums[i]
#             else:
#                 current_sum += nums[i]
#             if current_sum < min_subarr:
#                 min_subarr = current_sum

#         total_sum -= (min_subarr)
#         if min_subarr == total_sum:
#             return 
#         return total_sum 