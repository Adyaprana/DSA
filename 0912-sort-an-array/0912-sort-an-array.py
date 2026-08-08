# Merge Sort:
class Solution(object):
    def sortArray(self, nums):
        def merge_sort(nums):

            if len(nums) <= 1:
                return nums

            # Split
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            # Recursive calls
            left = merge_sort(left)
            right = merge_sort(right)

            # Merge
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                    result.append(right[j])
                    j += 1
            return result

        return merge_sort(nums)
