class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        HashMap = {0:1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            need = prefix_sum - k
            if need in HashMap:
                count += HashMap[need]
            HashMap[prefix_sum] = HashMap.get(prefix_sum, 0) + 1
        return count 


# class Solution(object):
#     def subarraySum(self, nums, k):
#         count = 0
#         for start in range(len(nums)):
#             current_sum = 0
#             for i in range(start, len(nums)):
#                 current_sum += nums[i]
#                 if current_sum == k:
#                     count += 1
#         return count