# HashSet — Optimal O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        seen = set(nums)
        count = 0
        current_count = 0
        for num in seen:
            if num - 1 not in seen:
                current_count = 1 
                current = num
                while current+1 in seen:
                    current += 1
                    current_count += 1
                if current_count > count:
                    count = current_count
        return count

# Sorting O(n log n)
# class Solution(object):
#     def longestConsecutive(self, nums):

#         if len(nums) == 0:
#             return 0
#         nums.sort()
#         current_count = 1
#         count = 1

#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 continue
#             elif nums[i] == nums[i - 1] + 1:
#                 current_count += 1
#             else:
#                 current_count = 1
#             if current_count > count:
#                 count = current_count
#         return count

